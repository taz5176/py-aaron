from argparse import ArgumentParser, HelpFormatter, _SubParsersAction


class NoSubparsersMetavarFormatter(HelpFormatter):

    def _format_action(self, action):
        result = super(NoSubparsersMetavarFormatter,
                       self)._format_action(action)
        if isinstance(action, _SubParsersAction):
            return "%*s%s" % (self._current_indent, "", result.lstrip())
        return result

    def _format_action_invocation(self, action):
        if isinstance(action, _SubParsersAction):
            return ""
        return super(NoSubparsersMetavarFormatter,
                     self)._format_action_invocation(action)

    def _iter_indented_subactions(self, action):
        if isinstance(action, _SubParsersAction):
            try:
                get_subactions = action._get_subactions
            except AttributeError:
                pass
            else:
                for subaction in get_subactions():
                    yield subaction
        else:
            for subaction in super(NoSubparsersMetavarFormatter,
                                   self)._iter_indented_subactions(action):
                yield subaction


parser = ArgumentParser(formatter_class=NoSubparsersMetavarFormatter)
subparsers = parser.add_subparsers(title="commands")

foo = subparsers.add_parser("foo", help="- foo does foo")
bar = subparsers.add_parser("bar", help="- bar does bar")

parser.parse_args(['-h'])