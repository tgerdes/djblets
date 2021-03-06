#
# forms.py -- Form classes useful for extensions
#
# Copyright (c) 2010-2011  Beanbag, Inc.
# Copyright (c) 2008-2010  Christian Hammond
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from django import forms


class SettingsForm(forms.Form):
    """Settings form for extension configuration.

    A base form for loading/saving settings for an extension. This is meant
    to be overridden by extensions to provide configuration pages. Any fields
    defined by the form will be loaded and saved automatically.
    """
    def __init__(self, extension, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        self.extension = extension

        for field in self.fields:
            if field in self.extension.settings:
                self.fields[field].initial = self.extension.settings[field]

    def save(self):
        if not self.errors:
            for key, value in self.cleaned_data.iteritems():
                self.extension.settings[key] = value

            self.extension.settings.save()
