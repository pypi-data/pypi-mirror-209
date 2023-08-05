# AUTOGENERATED FILE! PLEASE DON'T EDIT
from .callbacks import Callback, Callbacks, Cbs
import k1lib
import matplotlib.pyplot as plt
from functools import partial
from typing import List, Tuple, Callable, Union
try: import torch; import torch.nn as nn; hasTorch = True
except:
    torch = k1lib.Object().withAutoDeclare(lambda: type("RandomClass", (object, ), {}))
    nn = k1lib.Object().withAutoDeclare(lambda: type("RandomClass", (object, ), {})); hasTorch = False
__all__ = ["HookParam"]
class ParamData(k1lib.Object):
    def __init__(self):
        super().__init__()
        self.means = []; self.stds = []
        self.mins = []; self.maxs = []
    def update(self, torchParam:nn.Parameter):
        self.means.append(torchParam.mean().item())
        self.stds.append(torchParam.std().item())
        self.mins.append(torchParam.min().item())
        self.maxs.append(torchParam.max().item())
    def __len__(self): return len(self.means)
    def __repr__(self):
        return f"""Param's saved data. Use...
- d.means: to get list of means
- d.stds: to get list of means
- d.mins: to get list of mins
- d.maxs: to get list of maxs"""
class Param:
    def __init__(self, name:str, torchParam:nn.Parameter):
        self.name = name
        self.torchParam = torchParam
        self.data = ParamData()
        self.every = k1lib.Every(3)
    def update(self):
        if self.every(): self.data.update(self.torchParam.detach())
    def __repr__(self):
        return f"""Param `{self.name}`. Use...
- p.torchParam: to get actual underlying parameter
- p.data: to get data stored
- cb.plot(): to quickly look at everything"""
@k1lib.patch(Cbs)
class HookParam(Callback):
    """Records means and stds of all parameters"""
    def __init__(self):
        ""
        super().__init__(); self.params:List[Param] = []
    def __getitem__(self, idx:Union[int, slice]):
        if type(idx) == int: return self.params[idx]
        answer = HookParam(); answer.params = self.params[idx]; return answer
    def __len__(self): return len(self.params)
    def _selected(self, paramName:str):
        splits = paramName.split(".")
        try:
            mS = self.l.selector
            for split in splits[:-1]: mS = mS[split]
            return "HookParam" in mS and hasattr(mS, splits[-1])
        except KeyError: return False
    def startRun(self):
        if len(self) == 0: # set things up first time only
            self.params = [Param(k, v) for k, v in self.l.model.named_parameters() if self._selected(k)]
    def startBatch(self): [param.update() for param in self.params]
    def css(self, css:str):
        """Creates a new HookParam object with selected modules. May be useful
for displaying a subset of the recorded data"""
        oldSelector = self.l.selector; answer = HookParam()
        self.l.selector = k1lib.selector.select(self.l.model, css)
        answer.params = [param for param in self.params if self._selected(param.name)]
        self.l.selector = oldSelector; return answer
    def __repr__(self):
        s = f", {len(self[0].data)} means and stds each" if len(self) > 0 else ""
        names = "\n".join([f"  {i}. {p.name}" for i, p in enumerate(self)])
        return f"""{super()._reprHead}: {len(self)} params{s}:\n{names}\n
Use...
- p.plot(): to quickly look at everything
- p[i]: to view a single param
- p[a:b]: to get a new HookParam with selected params
- p.css("..."): to select a specific subset of modules only
{super()._reprCan}"""
def plotF(params:Union[HookParam, Param, List[Param]], rangeSlice:slice):
    if type(params) == Param: params = [params]
    fields = params[0].data.state.keys(); step = rangeSlice.step or 1
    fig, axes = plt.subplots(2, 2, figsize=(10, 6), dpi=100)
    axes = axes.flatten()
    for field, ax in zip(fields, axes):
        for param in params:
            fieldData = param.data[field]
            r = k1lib.Range(len(fieldData))[rangeSlice]
            ax.plot(r.range_[::step], fieldData[r.slice_][::step])
        ax.set_title(field.capitalize())
    plt.figlegend([p.name for p in params], loc='right')
@k1lib.patch(HookParam)
@k1lib.patch(Param)
def plot(self): return k1lib.viz.SliceablePlot(partial(plotF, self))