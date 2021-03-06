# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from django import forms


class AddonRecommendationsForm(forms.Form):
    client_id = forms.UUIDField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    num_items = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1,
        max_value=50,
        initial=10,
        required=True
    )
