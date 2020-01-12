"""Defines core module class."""

from .module import VoluxModule
from .demo import VoluxDemo
from typing import List, Any, Dict, Iterator, Type, Union


class VoluxCore(VoluxModule):
    """Provides a set of utilities for use in other modules."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Instansiate voluxcore module."""
        super().__init__(
            module_name="Volux Core",
            module_attr="core",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            module_setup=self._setup,
            module_cleanup=self._cleanup,
            shared_modules=[],
            pollrate=0,
        )
        self.val: int = 0

    def get(self) -> int:  # pylint: disable=method-hidden
        """Get stored value."""
        return self.val

    def set(self, new_val: int) -> None:  # pylint: disable=method-hidden
        """Set stored value."""
        self.val = new_val

    def _setup(self) -> None:  # pylint: disable=method-hidden

        pass

    def _cleanup(self) -> None:  # pylint: disable=method-hidden

        pass

    def get_python_module_items(self, module: Any) -> Iterator[Any]:
        """Get all items for a given module, i.e. return result of dir(module)."""

        def map_module_items(item_name: str) -> Any:
            return getattr(module, item_name)

        module_items: Iterator[Any] = map(map_module_items, dir(module))

        return module_items

    def filter_by_attr_value(
        self, items: List[Any], attribute: str, attribute_value: Any
    ) -> Iterator[Any]:
        """Return only items which have [item].[attribute] == [attribute_value]."""

        def filter_attribs(item: Any) -> Any:
            if hasattr(item, attribute):
                if getattr(item, attribute) == attribute_value:
                    return item

        valid_items: Iterator[Any] = filter(filter_attribs, items)

        return valid_items

    def filter_by_superclass(self, items: Any, superclass: Any) -> Any:
        """Return all objects which have inherited a particular superclass."""
        return self.filter_by_attr_value(items, "superclass", superclass)

    def _map_demo_aliases(self, demo: VoluxDemo) -> str:
        demoInstance: VoluxDemo = demo()  # type: ignore
        return demoInstance._alias

    def gen_demo_dict(
        self, demo_list: List[VoluxDemo] = []
    ) -> Dict[str, VoluxDemo]:
        """Turn a list for VoluxDemos into a dictionary of {[demo alias]: [demo]} pairs.

        If demo_list is not supplied, use own method to get list of available demos
        """
        if len(demo_list) == 0:
            demo_dict = {
                self._map_demo_aliases(demo): demo for demo in self.get_demos()
            }
        else:
            demo_dict = {demo._alias: demo for demo in demo_list}
        return demo_dict

    def get_demos(self) -> List[VoluxDemo]:
        """Return all valid Volux demos found in demos folder."""
        from volux import demos, VoluxDemo, VoluxCore

        demos_collected = []

        for attrib in dir(demos):

            demo = getattr(demos, attrib)

            if type(demo) is type:

                if issubclass(demo, VoluxDemo) is True:

                    demos_collected.append(demo)

        return demos_collected

    def get_demo_aliases(self) -> Iterator[str]:
        """Return a list aliases of all valid Volux demos found in demos folder."""
        demos_collected = self.get_demos()

        demo_aliases = map(self._map_demo_aliases, demos_collected)
        return demo_aliases

    def get_script_names(self) -> Iterator[str]:
        """Return a list of names of scripts found in the scripts folder."""
        from volux import scripts

        def filter_scripts(item_name: str) -> Union[str, None]:
            if "script_" in item_name:
                return item_name
            else:
                return None

        return filter(filter_scripts, dir(scripts))
