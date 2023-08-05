from PIL import Image
# > Graphics
from PIL.Image import Resampling
from ripix import AsyncPixels, Pixels
from rich.progress import Progress, BarColumn, TextColumn
from textual.widgets import Static, Label, ListItem, ListView, Input, TextLog
# > Typing
from typing import Optional, Tuple, TypeVar, Union, Any, Dict
# > Local Import's
from .types import MusicList
from .codeсbase import CodecBase
from .functions import (
    aiter,
    get_bar_status,
    get_sound_basename
)

# ! Types
T = TypeVar('T')

# ! Music List
class MusicListViewItem(ListItem):
    def __init__(
        self,
        title: str="",
        first_subtitle: str="",
        second_subtitle: str="",
        sound_uuid: Optional[str]=None
    ) -> None:
        super().__init__(classes="music-list-view-item")
        self.title_label = Label(title, classes="music-list-view-item-title-label")
        self.first_subtitle_label = Label(f" {first_subtitle}", classes="music-list-view-item-subtitle-label")
        self.second_subtitle_label = Label(f" {second_subtitle}", classes="music-list-view-item-subtitle-label")
        self.sound_uuid = sound_uuid
        
        self.compose_add_child(self.title_label)
        self.compose_add_child(self.first_subtitle_label)
        self.compose_add_child(self.second_subtitle_label)
    
    async def update_labels(
        self,
        title: Optional[str]=None,
        first_subtitle: Optional[str]=None,
        second_subtitle: Optional[str]=None,
    ) -> None:
        if title is not None: self.title_label.update(title)
        if first_subtitle is not None: self.first_subtitle_label.update(title)
        if second_subtitle is not None: self.second_subtitle_label.update(title)

class MusicListView(ListView):
    def __init__(self, **kwargs) -> None:
        kwargs["classes"] = "music-list-view"
        super().__init__(**kwargs)
        self.music_list: MusicList = MusicList()
    
    def add_sound(self, sound: CodecBase) -> str:
        sound_uuid = self.music_list.add(sound)
        self.append(
            MusicListViewItem(
                f"{get_sound_basename(sound)}",
                "{duration} sec, {channel_mode}, {samplerate} Hz, {bitrate} kbps".format(
                    duration=round(sound.duration),
                    channel_mode="Mono" if sound.channels <= 1 else "Stereo",
                    samplerate=round(sound.samplerate),
                    bitrate=round(sound.bitrate / 1000)
                ),
                sound.name,
                sound_uuid
            )
        )
        return sound_uuid
    
    def get_sound(self, sound_uuid: str) -> Optional[CodecBase]: return self.music_list.get(sound_uuid)
    
    async def aio_add_sound(self, sound: CodecBase):
        sound_uuid = await self.music_list.aio_add(sound)
        await self.append(
            MusicListViewItem(
                f"{get_sound_basename(sound)}",
                "{duration} sec, {channel_mode}, {samplerate} Hz, {bitrate} kbps, {codec_name}".format(
                    duration=round(sound.duration),
                    channel_mode="Mono" if sound.channels <= 1 else "Stereo",
                    samplerate=round(sound.samplerate),
                    bitrate=round(sound.bitrate / 1000),
                    codec_name=sound.codec_name
                ),
                sound.name,
                sound_uuid
            )
        )
        return sound_uuid
    
    def get_items_count(self) -> int: return len(self.children)
    def exists_item_index(self, index: int) -> bool: return 0 >= index < self.get_items_count()
    def get_item_index_from_sound_uuid(self, sound_uuid: str) -> Optional[int]:
        item: MusicListViewItem
        for idx, item in enumerate(self.children):
            if item.sound_uuid == sound_uuid:
                return idx
    
    def get_item_from_index(self, index: int) -> Optional[MusicListViewItem]:
        try: return self.children[index]
        except:
            try: return self.children[0]
            except: pass
    
    def get_next_sound_uuid(self, sound_uuid: str) -> Optional[str]:
        if (index:=self.get_item_index_from_sound_uuid(sound_uuid)) is not None:
            if (mli:=self.get_item_from_index(index+1)) is not None:
                return mli.sound_uuid
    
    def select_list_item_from_sound_uuid(self, sound_uuid: str) -> None:
        try:
            super()._on_list_item__child_clicked(
                ListItem._ChildClicked(
                    self.children[self.get_item_index_from_sound_uuid(sound_uuid)]
                )
            )
        except: pass
    
    async def aio_get_item_from_index(self, index: int) -> Optional[MusicListViewItem]:
        try: return self.children[index]
        except:
            try: return self.children[0]
            except: pass
    
    async def aio_get_item_index_from_sound_uuid(self, sound_uuid: str) -> Optional[int]:
        item: MusicListViewItem
        async for idx, item in aiter(enumerate(self.children)):
            if item.sound_uuid == sound_uuid:
                return idx
    
    async def aio_get_next_sound_uuid(self, sound_uuid: str) -> Optional[str]:
        if (index:=await self.aio_get_item_index_from_sound_uuid(sound_uuid)) is not None:
            if (mli:=await self.aio_get_item_from_index(index+1)) is not None:
                return mli.sound_uuid
    
    async def aio_select_list_item_from_sound_uuid(self, sound_uuid: str) -> None:
        try:
            super()._on_list_item__child_clicked(
                ListItem._ChildClicked(
                    self.children[await self.aio_get_item_index_from_sound_uuid(sound_uuid)]
                )
            )
        except: pass

# ! ProgressBar
class IndeterminateProgress(Static):
    def __init__(self, getfunc=get_bar_status, fps: int=15):
        super().__init__("", classes="indeterminate-progress-bar")
        self._bar = Progress(BarColumn(), TextColumn("{task.description}"))
        self._task_id = self._bar.add_task("", total=None)
        self._fps = fps
        self._getfunc = getfunc
    
    def on_mount(self) -> None:
        self.update_render = self.set_interval(1/self._fps, self.update_progress_bar)
    
    async def upgrade_task(self, description: str="", completed: Optional[float]=None, total: Optional[float]=None) -> None:
        self._bar.update(self._task_id, total=total, completed=completed, description=description)
    
    async def update_progress_bar(self) -> None:
        d, c, t = await self._getfunc()
        if self._bar.columns[0].bar_width != (self.size[0]-len(d)-1):
            self._bar.columns[0].bar_width = self.size[0]-len(d)-1
        
        await self.upgrade_task(completed=c, total=t, description=d)
        self.update(self._bar)

# ! Image Label
class StandartImageLabel(Label):
    def __init__(
        self,
        default_image: Image.Image,
        image: Optional[Image.Image]=None,
        fps: int=2,
        *,
        resample: Resampling=Resampling.NEAREST
    ):
        super().__init__("<image not found>", classes="image-label")
        self.image_resample = resample
        self.default_image: Image.Image = default_image
        self.image: Optional[Image.Image] = image
        self.image_text: Union[str, Pixels] = "<image not found>"
        self.last_image_size: Optional[Tuple[int, int]] = None
        self._fps = fps
    
    def on_mount(self) -> None:
        self.update_render = self.set_interval(1/self._fps, self.update_image_label)
    
    async def update_image_label(self):
        image, resample = (self.default_image, Resampling.NEAREST) if (self.image is None) else (self.image, self.image_resample)
        
        new_size = (self.size[0], self.size[1])
        if self.last_image_size != new_size:
            self.image_text = Pixels.from_image(image, new_size, resample)
            self.last_image_size = new_size
        
        self.update(self.image_text)
    
    async def update_image(self, image: Optional[Image.Image]=None) -> None:
        self.image = image
        
        image, resample = (self.default_image, Resampling.NEAREST) if (self.image is None) else (self.image, self.image_resample)
        self.image_text = Pixels.from_image(image, (self.size[0], self.size[1]), resample)

class AsyncImageLabel(Label):
    def __init__(
        self,
        default_image: Image.Image,
        image: Optional[Image.Image]=None,
        fps: int=2,
        *,
        resample: Resampling=Resampling.NEAREST
    ):
        super().__init__("<image not found>", classes="image-label")
        self.image_resample = resample
        self.default_image: Image.Image = default_image
        self.image: Optional[Image.Image] = image
        self.image_text: Union[str, AsyncPixels] = "<image not found>"
        self.last_image_size: Optional[Tuple[int, int]] = None
        self._fps = fps
    
    def on_mount(self) -> None:
        self.update_render = self.set_interval(1/self._fps, self.update_image_label)
    
    async def update_image_label(self):
        image, resample = (self.default_image, Resampling.NEAREST) if (self.image is None) else (self.image, self.image_resample)
        
        new_size = (self.size[0], self.size[1])
        if self.last_image_size != new_size:
            self.image_text = await AsyncPixels.from_image(image, new_size, resample)
            self.last_image_size = new_size
        
        self.update(self.image_text)
    
    async def update_image(self, image: Optional[Image.Image]=None) -> None:
        self.image = image
        
        image, resample = (self.default_image, Resampling.NEAREST) if (self.image is None) else (self.image, self.image_resample)
        self.image_text = await AsyncPixels.from_image(image, (self.size[0], self.size[1]), resample)


# ! Input Field Functions
async def _conv(value: str) -> Tuple[bool, Optional[Any]]: return True, value
async def _submit(input: Input, value: Any) -> None: ...
def _update_placeholder() -> Optional[str]: ...

# ! Input Field
class InputField(Input):
    def __init__(
        self,
        conv=_conv,
        submit=_submit,
        update_placeholder=_update_placeholder,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self._conv = conv
        self._submit = submit
        self._update_placeholder = update_placeholder
        if (placeholder:=self._update_placeholder()) is not None:
            self.placeholder = placeholder
    
    async def action_submit(self):
        value = self.value
        self.value = ""
        if value.replace(" ", "") != "":
            ok, c_value = await self._conv(value)
            if ok: await self._submit(self, c_value)
        if (placeholder:=self._update_placeholder()) is not None:
            self.placeholder = placeholder

# ! Configurate List
class ConfigurateListItem(ListItem):
    def __init__(
        self,
        *children,
        title: str="",
        desc: str="",
        **kwargs
    ):
        kwargs["classes"] = "configurate-list-view-item"
        super(ConfigurateListItem, self).__init__(*children, **kwargs)
        self.border_title = title
        self.border_subtitle = desc
    
    async def updating(self, title: Optional[str]="", desc: Optional[str]="") -> None:
        if title is not None: self.border_title = title
        if desc is not None: self.border_subtitle = desc

class ConfigurateListView(ListView):
    def __init__(self, *children, **kwargs):
        kwargs["classes"] = "configurate-list-view"
        super().__init__(*children, **kwargs)
        self.border_title = "Configurate"

# ! Log Menu
class LogMenu(TextLog):
    def __init__(self, enable_logging: bool=True, **kwargs):
        self.enable_logging = enable_logging
        if kwargs.get("classes", None) is not None:
            kwargs["classes"] = kwargs["classes"] + " log-menu -hidden"
        else:
            kwargs["classes"] = "log-menu -hidden"
        super().__init__(**kwargs)
    
    def wlog(self, chap: str, msg: str, *, cc: str="green") -> None:
        if self.enable_logging:
            self.write(f"[[{cc}]{chap.center(8)}[/]]: {msg}\n")
