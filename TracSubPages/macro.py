"""
TracSubPages: A Trac macro that displays the bodies of wiki pages
              inside other wiki pages

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from trac.core import TracError
from trac.util.html import Markup
from trac.wiki.formatter import format_to_html
from trac.wiki.macros import WikiMacroBase


class SubPageMacro(WikiMacroBase):
    """A Trac macro to display bodies of other wiki pages inline."""

    def expand_macro(self, formatter, name, content):
        args = content.split(',')
        num_args = len(args)

        if not (1 <= num_args <= 2):
            raise TracError('Incorrect number of arguments (two required). '
                            'Usage: [[subpage(page, [true/false])]] where '
                            'true/false determines whether or not an Edit '
                            'Section link is shown.')

        page_name = args[0].strip()

        if num_args == 2:
            edit_link = args[1].lower().strip()
            if edit_link not in ('true', 'false'):
                raise TracError('Incorrect second argument (should be "true" '
                                'or "false"). Usage: [[subpage(true/false, '
                                'page)]] where true/false determines whether '
                                'or not an Edit Section link is shown.')
            edit_link = edit_link == 'true'

        else:
            edit_link = True

        # TODO: The error raised if the wiki page
        #       doesn't exist isn't descriptive at all
        wikiparser = formatter.wikiparser
        target_url = wikiparser.link_resolvers['wiki'](formatter,
                                                       'wiki',
                                                       page_name,
                                                       None).attrib.get('href')

        wiki_body = ''
        for page_text, in self.env.db_query("""
                SELECT text FROM wiki WHERE wiki.name=%s
                ORDER BY wiki.version DESC LIMIT 1
                """, (page_name,)):
            wiki_body = format_to_html(self.env, formatter.context, page_text)
            break

        link_tag = Markup('<p><a href="%s?action=edit" class="wiki">'
                          'Edit Section</a></p>' % target_url)

        return wiki_body + (link_tag if edit_link else '')
