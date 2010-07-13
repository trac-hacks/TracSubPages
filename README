Overview
========

TracSubPages is a Trac plugin that supplies a macro allowing full wiki pages to be displayed inside of other wiki pages. This is useful if there is a piece of content (such as a contact table or log) that needs to be displayed in multiple places, as it eliminates the need for each instance of this content to be maintained.

Usage
-----

The syntax for the subpage macro is simple::

[[subpage(wiki_page, [show_link])]]

Where `wiki_page` is the wiki page (No url is needed here, nor 'wiki/', just the page). The macro supports pages that aren't top-level, too ('BigCategory/SpecificSubject'). The second argument, `showlink` is an optional argument (`true` or `false`) that determines whether or not a link to edit the rendered page will be shown at the bottom of the subpage section (The link reads 'Edit Section' and provides a link directly to the edit page of the referenced wiki page). 

For example, if a user had created a wiki pages called 'Minutes' and wanted to display it inline in another wiki page without a link to edit it, he or she would add the following entry to the wiki page that is intended to display the extra content::

[[subpage(Minutes, False)]]

If the user later decided that he or she wanted a link to be placed at the bottom of the inline section for quick editing, the entry should be changed as follows::

[[subpage(Minutes)]]

Note that the second boolean argument 'True' is not needed, as it is assumed by default.

Limitations
-----------

 * A wiki page needs to exist before you link to it with a subpage macro. This may seem obvious, but the error caused by a broken link isn't very descriptive (yet).
 * Please use only wiki formatting for subpages. The use of macros can (and probably will) cause errors.
