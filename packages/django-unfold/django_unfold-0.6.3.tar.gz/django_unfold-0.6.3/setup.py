# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['unfold',
 'unfold.contrib',
 'unfold.contrib.filters',
 'unfold.contrib.forms',
 'unfold.contrib.import_export',
 'unfold.templatetags']

package_data = \
{'': ['*'],
 'unfold': ['static/unfold/css/*',
            'static/unfold/js/*',
            'templates/admin/*',
            'templates/admin/auth/user/*',
            'templates/admin/edit_inline/*',
            'templates/admin/includes/*',
            'templates/admin/widgets/*',
            'templates/auth/widgets/*',
            'templates/registration/*',
            'templates/unfold/helpers/*',
            'templates/unfold/helpers/messages/*',
            'templates/unfold/layouts/*',
            'templates/unfold/widgets/*'],
 'unfold.contrib.filters': ['static/unfold/filters/css/*',
                            'static/unfold/filters/js/*',
                            'templates/unfold/filters/*'],
 'unfold.contrib.forms': ['static/unfold/forms/css/*',
                          'static/unfold/forms/js/*',
                          'templates/unfold/forms/*',
                          'templates/unfold/forms/helpers/*'],
 'unfold.contrib.import_export': ['templates/admin/import_export/*']}

install_requires = \
['django>=3.2']

setup_kwargs = {
    'name': 'django-unfold',
    'version': '0.6.3',
    'description': 'Clean & minimal Django admin theme based on Tailwind CSS',
    'long_description': '![Screenshot - Objects Listing](https://github.com/unfoldadmin/django-unfold/raw/main/screenshot-1.jpg)\n\n![Screenshot - Login Page](https://github.com/unfoldadmin/django-unfold/raw/main/screenshot-2.jpg)\n\n## Unfold Django Admin Theme\n\nUnfold is a new theme for Django Admin incorporating some most common practises for building full-fledged admin areas.\n\n- **Visual**: provides new user interface based on Tailwind CSS framework\n- **Sidebar:** simplifies definition of custom sidebar navigation\n- **Dark mode:** supports both light and dark mode versions\n- **Configuration:** most of the basic options can be changed in settings.py\n- **Dependencies:** completely based only on `django.contrib.admin`\n- **Filters:** custom widgets for filters (e.g. numeric filter)\n- **Actions:** multiple ways how to define actions within different parts of admin\n\n## Table of Contents\n\n- [Unfold Django Admin Theme](#unfold-django-admin-theme)\n- [Table of Contents](#table-of-contents)\n- [Installation](#installation)\n- [Configuration](#configuration)\n  - [Available settings.py options](#available-settingspy-options)\n  - [Available unfold.admin.ModelAdmin options](#available-unfoldadminmodeladmin-options)\n- [Decorators](#decorators)\n  - [@display](#display)\n- [Actions](#actions)\n  - [Actions overview](#actions-overview)\n  - [Custom unfold @action decorator](#custom-unfold-action-decorator)\n  - [Action handler functions](#action-handler-functions)\n    - [For submit row action](#for-submit-row-action)\n    - [For global, row and detail action](#for-global-row-and-detail-action)\n  - [Action examples](#action-examples)\n- [Filters](#filters)\n- [Third party packages](#third-party-packages)\n  - [django-import-export](#django-import-export)\n- [User Admin Form](#user-admin-form)\n- [Adding Custom Styles and Scripts](#adding-custom-styles-and-scripts)\n- [Project Level Tailwind Stylesheet](#project-level-tailwind-stylesheet)\n- [Custom Admin Dashboard](#custom-admin-dashboard)\n- [Unfold Development](#unfold-development)\n  - [Pre-commit](#pre-commit)\n  - [Poetry Configuration](#poetry-configuration)\n  - [Compiling Tailwind](#compiling-tailwind)\n\n## Installation\n\nThe installation process is minimal. Everything what is needed after installation is to put new application at the beginning of **INSTALLED_APPS**. Default admin configuration in urls.py can stay as it is and there are no changes required.\n\n```python\n# settings.py\n\nINSTALLED_APPS = [\n    "unfold",  # before django.contrib.admin\n    "unfold.contrib.filters",  # optional, if special filters are needed\n    "unfold.contrib.forms",  # optional, if special form elements are needed\n    "unfold.contrib.import_export",  # optional, if django-import-export package is used\n    "django.contrib.admin",  # required\n]\n```\n\nIn case you need installation command below are the versions for `pip` and `poetry` which needs to be executed in shell.\n\n```bash\npip install django-unfold\npoetry add django-unfold\n```\n\nJust for an example below is the minimal admin configuration in terms of adding Unfold into URL paths.\n\n```python\n# urls.py\n\nfrom django.contrib import admin\nfrom django.urls import path\n\nurlpatterns = [\n    path("admin/", admin.site.urls),\n    # Other URL paths\n]\n```\n\nAfter installation, it is required that admin classes are going to inherit from custom `ModelAdmin` available in `unfold.admin`.\n\n```python\n# admin.py\n\nfrom django.contrib import admin\nfrom unfold.admin import ModelAdmin\n\n\n@admin.register(MyModel)\nclass CustomAdminClass(ModelAdmin):\n    pass\n```\n\n**Note:** Registered admin models coming from third party packages are not going to properly work with Unfold because of parent class. By default, these models are registered by using `django.contrib.admin.ModelAdmin` but it is needed to use `unfold.admin.ModelAdmin`. Solution for this problem is to unregister model and then again register it back by using `unfold.admin.ModelAdmin`.\n\n```python\n# admin.py\nfrom django.contrib import admin\nfrom django.contrib.auth.admin import UserAdmin as BaseUserAdmin\nfrom django.contrib.auth.models import User\n\nfrom unfold.admin import ModelAdmin\n\n\nadmin.site.unregister(User)\n\n\n@admin.register(User)\nclass UserAdmin(BaseUserAdmin, ModelAdmin):\n    pass\n```\n\n## Configuration\n\n### Available settings.py options\n\n```python\n# settings.py\n\nfrom django.templatetags.static import static\nfrom django.urls import reverse_lazy\nfrom django.utils.translation import gettext_lazy as _\n\nUNFOLD = {\n    "SITE_TITLE": None,\n    "SITE_HEADER": None,\n    "SITE_URL": "/",\n    "SITE_ICON": lambda request: static("logo.svg"),\n    "SITE_SYMBOL": "speed",  # symbol from icon set\n    "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",\n    "LOGIN": {\n        "image": lambda r: static("sample/login-bg.jpg"),\n        "redirect_after": lambda r: reverse_lazy("admin:APP_MODEL_changelist"),\n    },\n    "STYLES": [\n        lambda request: static("css/style.css"),\n    ],\n    "SCRIPTS": [\n        lambda request: static("js/script.js"),\n    ],\n    "COLORS": {\n        "primary": {\n            "50": "250 245 255",\n            "100": "243 232 255",\n            "200": "233 213 255",\n            "300": "216 180 254",\n            "400": "192 132 252",\n            "500": "168 85 247",\n            "600": "147 51 234",\n            "700": "126 34 206",\n            "800": "107 33 168",\n            "900": "88 28 135",\n        },\n    },\n    "EXTENSIONS": {\n        "modeltranslation": {\n            "flags": {\n                "en": "🇬🇧",\n                "fr": "🇫🇷",\n                "nl": "🇧🇪",\n            },\n        },\n    },\n    "SIDEBAR": {\n        "show_search": False,  # Search in applications and models names\n        "show_all_applications": False,  # Dropdown with all applications and models\n        "navigation": [\n            {\n                "title": _("Navigation"),\n                "separator": True,  # Top border\n                "items": [\n                    {\n                        "title": _("Dashboard"),\n                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons\n                        "link": reverse_lazy("admin:index"),\n                        "badge": "sample_app.badge_callback",\n                    },\n                    {\n                        "title": _("Users"),\n                        "icon": "people",\n                        "link": reverse_lazy("admin:users_user_changelist"),\n                    },\n                ],\n            },\n        ],\n    },\n    "TABS": [\n        {\n            "models": [\n                "app_label.model_name_in_lowercase",\n            ],\n            "items": [\n                {\n                    "title": _("Your custom title"),\n                    "link": reverse_lazy("admin:app_label_model_name_changelist"),\n                },\n            ],\n        },\n    ],\n}\n\n\ndef dashboard_callback(request, context):\n    """\n    Callback to prepare custom variables for index template which is used as dashboard\n    template. It can be overridden in application by creating custom admin/index.html.\n    """\n    context.update(\n        {\n            "sample": "example",  # this will be injected into templates/admin/index.html\n        }\n    )\n    return context\n\n\ndef badge_callback(request):\n    return 3\n```\n\n### Available unfold.admin.ModelAdmin options\n\n```python\nfrom django import models\nfrom django.contrib import admin\n\nfrom unfold.admin import ModelAdmin\nfrom unfold.contrib.forms.widgets import WysiwygWidget\n\n\n@admin.register(MyModel)\nclass CustomAdminClass(ModelAdmin):\n    # Preprocess content of readonly fields before render\n    readonly_preprocess_fields = {\n        "model_field_name": "html.unescape",\n        "other_field_name": lambda content: content.strip(),\n    }\n\n    # Display submit button in filters\n    list_filter_submit = False\n\n    # Custom actions\n    actions_list = []  # Displayed above the results list\n    actions_row = []  # Displayed in a table row in results list\n    actions_detail = []  # Displayed at the top of for in object detail\n    actions_submit_line = []  # Displayed near save in object detail\n\n    formfield_overrides = {\n        models.TextField: WysiwygWidget,\n    }\n```\n\n## Decorators\n\n### @display\n\nUnfold introduces it\'s own `unfold.decorators.display` decorator. By default it has exactly same behavior as native `django.contrib.admin.decorators.display` but it adds same customizations which helps to extends default logic.\n\n`@display(label=True)`, `@display(label={"value1": "success"})` displays a result as a label. This option fits for different types of statuses. Label can be either boolean indicating we want to use label with default color or dict where the dict is responsible for displaying labels in different colors. At the moment these color combinations are supported: success(green), info(blue), danger(red) and warning(orange).\n\n`@display(header=True)` displays in results list two information in one table cell. Good example is when we want to display customer information, first line is going to be customer\'s name and right below the name display corresponding email address. Method with such a decorator is supposed to return a list with two elements `return "Full name", "E-mail address"`.\n\n```python\n# models.py\n\nfrom django.db.models import TextChoices\nfrom django.utils.translation import gettext_lazy as _\n\nfrom unfold.admin import ModelAdmin\nfrom unfold.decorators import display\n\n\nclass UserStatus(TextChoices):\n    ACTIVE = "ACTIVE", _("Active")\n    PENDING = "PENDING", _("Pending")\n    INACTIVE = "INACTIVE", _("Inactive")\n    CANCELLED = "CANCELLED", _("Cancelled")\n\n\nclass UserAdmin(ModelAdmin):\n    list_display = [\n        "display_as_two_line_heading",\n        "show_status",\n        "show_status_with_custom_label",\n    ]\n\n    @display(\n        description=_("Status"),\n        ordering="status",\n        label=True,\n        mapping={\n            UserStatus.ACTIVE: "success",\n            UserStatus.PENDING: "info",\n            UserStatus.INACTIVE: "warning",\n            UserStatus.CANCELLED: "danger",\n        },\n    )\n    def show_status(self, obj):\n        return obj.status\n\n    @display(description=_("Status with label"), ordering="status", label=True)\n    def show_status_with_custom_label(self, obj):\n        return obj.status, obj.get_status_display()\n\n    @display(header=True)\n    def display_as_two_line_heading(self, obj):\n        return "First main heading", "Smaller additional description"\n```\n\n## Actions\n\nIt is highly recommended to read the base [Django actions documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/) before reading this section, since Unfold actions are derived from Django actions.\n\n### Actions overview\n\nBesides traditional actions selected from dropdown, Unfold supports several other types of actions. Following table\ngives overview of all available actions together with their recommended usage:\n\n| Type of action | Appearance                               | Usage                                                                                      | Examples of usage                      |\n| -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------- |\n| Default        | List view - top of listing (in dropdown) | Actions, where you want to select specific subset of instances to perform this action upon | Bulk deleting, bulk activation         |\n| Global         | List view - top of listing (as buttons)  | General actions for model, without selecting specific instances                            | Import, export                         |\n| Row            | List view - in each row                  | Action for one specific instance, executable from listing                                  | Activation, sync with external service |\n| Detail         | Detail view - top of detail              | Action for one specific instance, executable from detail                                   | Activation, sync with external service |\n| Submit line    | Detail view - near submit button         | Action performed during form submit (instance save)                                        | Publishing article together with save  |\n\n### Custom unfold @action decorator\n\nUnfold also uses custom `@action` decorator, supporting 2 more parameters in comparison to base `@action` decorator:\n\n- `url_path`: Action path name, used to override the path under which the action will be available\n  (if not provided, URL path will be generated by Unfold)\n- `attrs`: Dictionary of the additional attributes added to the `<a>` element, used for e.g. opening action in new tab (`{"target": "_blank"}`)\n\n### Action handler functions\n\nThis section provides explanation of how the action handler functions should be constructed for Unfold actions.\nFor default actions, follow official Django admin documentation.\n\n#### For submit row action\n\nSubmit row actions work a bit differently when compared to other custom Unfold actions.\nThese actions first invoke form save (same as if you hit `Save` button) and then lets you\nperform additional logic on already saved instance.\n\n#### For global, row and detail action\n\nAll these actions are based on custom URLs generated for each of them. Handler function for these views is\nbasically function based view.\n\nFor actions without intermediate steps, you can write all the logic inside handler directly. Request and object ID\nare both passed to these action handler functions, so you are free to fetch the instance from database and perform any\noperations with it. In the end, it is recommended to return redirect back to either detail or listing, based on where\nthe action was triggered from.\n\nFor actions with intermediate steps, it is recommended to use handler function only to redirect to custom URL with custom\nview. This view can be extended from base Unfold view, to have unified experience.\n\nIf that\'s confusing, there are examples for both these actions in next section.\n\n### Action examples\n\n```python\n# admin.py\n\nfrom django.db.models import Model\nfrom django.contrib.admin import register\nfrom django.shortcuts import redirect\nfrom django.urls import reverse_lazy\nfrom django.utils.translation import gettext_lazy as _\nfrom django.http import HttpRequest\nfrom unfold.admin import ModelAdmin\nfrom unfold.decorators import action\n\n\nclass User(Model):\n    pass\n\n\n@register(User)\nclass UserAdmin(ModelAdmin):\n    actions_list = ["changelist_global_action_import"]\n    actions_row = ["changelist_row_action_view_on_website"]\n    actions_detail = ["change_detail_action_block"]\n    actions_submit_line = ["submit_line_action_activate"]\n\n    @action(description=_("Save & Activate"))\n    def submit_line_action_activate(self, request: HttpRequest, obj: User):\n        """\n        If instance is modified in any way, it also needs to be saved,\n        since this handler is invoked after instance is saved.\n        :param request:\n        :param obj: Model instance that was manipulated, with changes already saved to database\n        :return: None, this handler should not return anything\n        """\n        obj.is_active = True\n        obj.save()\n\n    @action(description=_("Import"), url_path="import")\n    def changelist_global_action_import(self, request: HttpRequest):\n        """\n        Handler for global actions does not receive any queryset or object ids, because it is\n        meant to be used for general actions for given model.\n        :param request:\n        :return: View, as described in section above\n        """\n        # This is example of action redirecting to custom page, where the action will be handled\n        # (with intermediate steps)\n        return redirect(\n          reverse_lazy("view-where-import-will-be-handled")\n        )\n\n    @action(description=_("Row"), url_path="row-action", attrs={"target": "_blank"})\n    def changelist_row_action_view_on_website(self, request: HttpRequest, object_id: int):\n        """\n        Handler for list row action.\n        :param request:\n        :param object_id: ID of instance that this action was invoked for\n        :return: View, as described in section above\n        """\n        return redirect(f"https://example.com/{object_id}")\n\n    @action(description=_("Detail"), url_path="detail-action", attrs={"target": "_blank"})\n    def change_detail_action_block(self, request: HttpRequest, object_id: int):\n        """\n        Handler for detail action.\n        :param request:\n        :param object_id: ID of instance that this action was invoked for\n        :return: View, as described in section above\n        """\n        # This is example of action that handled whole logic inside handler\n        # function and redirects back to object detail\n        user = User.objects.get(pk=object_id)\n        user.block()\n        return redirect(\n            reverse_lazy("admin:users_user_change", args=(object_id,))\n        )\n```\n\n## Filters\n\nBy default, Django admin handles all filters as regular HTML links pointing at the same URL with different query parameters. This approach is for basic filtering more than enough. In the case of more advanced filtering by incorporating input fields, it is not going to work.\n\nCurrently, Unfold implements numeric filters inside `unfold.contrib.filters` application. In order to use these filters, it is required to add this application into `INSTALLED_APPS` in `settings.py` right after `unfold` application.\n\n```python\n# admin.py\n\nfrom django.contrib import admin\nfrom django.contrib.auth.models import User\n\nfrom unfold.admin import ModelAdmin\nfrom unfold.contrib.filters.admin import (\n    RangeNumericListFilter,\n    RangeNumericFilter,\n    SingleNumericFilter,\n    SliderNumericFilter,\n    RangeDateFilter,\n    RangeDateTimeFilter,\n)\n\n\nclass CustomSliderNumericFilter(SliderNumericFilter):\n    MAX_DECIMALS = 2\n    STEP = 10\n\n\nclass CustomRangeNumericListFilter(RangeNumericListFilter):\n    parameter_name = "items_count"\n    title = "items"\n\n\n@admin.register(User)\nclass YourModelAdmin(ModelAdmin):\n    list_filter_submit = True  # Submit button at the bottom of the filter\n    list_filter = (\n        ("field_A", SingleNumericFilter),  # Numeric single field search, __gte lookup\n        ("field_B", RangeNumericFilter),  # Numeric range search, __gte and __lte lookup\n        ("field_C", SliderNumericFilter),  # Numeric range filter but with slider\n        ("field_D", CustomSliderNumericFilter),  # Numeric filter with custom attributes\n        ("field_E", RangeDateFilter),  # Date filter\n        ("field_F", RangeDateTimeFilter),  # Datetime filter\n        CustomRangeNumericListFilter,  # Numeric range search not restricted to a model field\n    )\n\n    def get_queryset(self, request):\n        return super().get_queryset().annotate(items_count=Count("item", distinct=True))\n```\n\n## Third party packages\n\n### django-import-export\n\nTo get proper visual appearance for django-import-export, two things are needed\n\n1. Add `unfold.contrib.import_export` to `INSTALLED_APPS` at the begging of the file. This action will override all templates coming from the plugin.\n2. Change `import_form_class` and `export_form_class` in ModelAdmin which is inheriting from `ImportExportModelAdmin`. This chunk of code is responsible for adding proper styling to form elements.\n\n```python\nfrom unfold.admin import ModelAdmin\nfrom unfold.contrib.import_export.forms import ExportForm, ImportForm\n\nclass ExampleAdmin(ModelAdmin, ImportExportModelAdmin):\n    import_form_class = ImportForm\n    export_form_class = ExportForm\n```\n\n## User Admin Form\n\nUser\'s admin in Django is specific as it contains several forms which are requiring custom styling. All of these forms has been inherited and accordingly adjusted. In user admin class it is needed to use these inherited form classes to enable custom styling matching rest of the website.\n\n```python\n# models.py\n\nfrom django.contrib.admin import register\nfrom django.contrib.auth.models import User\nfrom django.contrib.auth.admin import UserAdmin as BaseUserAdmin\n\nfrom unfold.admin import ModelAdmin\nfrom unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm\n\n\n@register(User)\nclass UserAdmin(BaseUserAdmin, ModelAdmin):\n    form = UserChangeForm\n    add_form = UserCreationForm\n    change_password_form = AdminPasswordChangeForm\n```\n\n## Adding Custom Styles and Scripts\n\nTo add new custom styles, for example for custom dashboard, it is possible to load them via **STYLES** key in **UNFOLD** dict. This key accepts a list of strings or lambda functions which will be loaded on all pages. JavaScript files can be loaded by using similar apprach, but **SCRIPTS** is used.\n\n```python\n# settings.py\n\nfrom django.templatetags.static import static\n\nUNFOLD = {\n    "STYLES": [\n        lambda request: static("css/style.css"),\n    ],\n    "SCRIPTS": [\n        lambda request: static("js/script.js"),\n    ],\n}\n```\n\n## Project Level Tailwind Stylesheet\n\nWhen creating custom dashboard or adding custom components, it is needed to add own styles. Adding custom styles is described above. Most of the time, it is supposed that new elements are going to match with the rest of the administration panel. First of all, create tailwind.config.js in your application. Below is located minimal configuration for this file.\n\n```javascript\n// tailwind.config.js\n\nmodule.exports = {\n  content: ["./your_project/**/*.{html,py,js}"],\n  // In case custom colors are defined in UNFOLD["COLORS"]\n  colors: {\n    primary: {\n      100: "rgb(var(--color-primary-100) / <alpha-value>)",\n      200: "rgb(var(--color-primary-200) / <alpha-value>)",\n      300: "rgb(var(--color-primary-300) / <alpha-value>)",\n      400: "rgb(var(--color-primary-400) / <alpha-value>)",\n      500: "rgb(var(--color-primary-500) / <alpha-value>)",\n      600: "rgb(var(--color-primary-600) / <alpha-value>)",\n      700: "rgb(var(--color-primary-700) / <alpha-value>)",\n      800: "rgb(var(--color-primary-800) / <alpha-value>)",\n      900: "rgb(var(--color-primary-900) / <alpha-value>)",\n    },\n  },\n};\n```\n\nOnce the configuration file is set, it is possible to compile new styles which can be loaded into admin by using **STYLES** key in **UNFOLD** dict.\n\n```bash\nnpx tailwindcss  -o your_project/static/css/styles.css --watch --minify\n```\n\n## Custom Admin Dashboard\n\nThe most common thing which needs to be adjusted for each project in admin is the dashboard. By default Unfold does not provide any dashboard components. The default dashboard experience with list of all applications and models is kept with proper styling matching rest of the components but thats it. Anyway, Unfold was created that creation of custom dashboard will be streamlined.\n\nCreate `templates/admin/index.html` in your project and paste the base template below into it. By default, all your custom styles here are not compiled because CSS classes are located in your specific project. Here it is needed to set up the Tailwind for your project and all requried instructions are located in [Project Level Tailwind Stylesheet](#project-level-tailwind-stylesheet) chapter.\n\n```\n{% extends \'unfold/layouts/base_simple.html\' %}\n\n{% load cache humanize i18n %}\n\n{% block breadcrumbs %}{% endblock %}\n\n{% block title %}{% if subtitle %}{{ subtitle }} | {% endif %}{{ title }} | {{ site_title|default:_(\'Django site admin\') }}{% endblock %}\n\n{% block branding %}\n    <h1 id="site-name"><a href="{% url \'admin:index\' %}">{{ site_header|default:_(\'Django administration\') }}</a></h1>\n{% endblock %}\n\n{% block content %}\n    Start creating your own Tailwind components here\n{% endblock %}\n```\n\nNote: In case that it is needed to pass custom variables into dashboard tamplate, check **DASHOARD_CALLBACK** in **UNFOLD** dict.\n\n## Unfold Development\n\n### Pre-commit\n\nBefore adding any source code, it is recommended to have pre-commit installed on your local computer to check for all potential issues when comitting the code.\n\n```bash\npip install pre-commit\npre-commit install\npre-commit install --hook-type commit-msg\n```\n\n### Poetry Configuration\n\nTo add a new feature or fix the easiest approach is to use django-unfold in combination with Poetry. The process looks like:\n\n- Install django-unfold via `poetry add django-unfold`\n- After that it is needed to git clone the repository somewhere on local computer.\n- Edit _pyproject.toml_ and update django-unfold line `django-unfold = { path = "../django-unfold", develop = true}`\n- Lock and update via `poetry lock && poetry update`\n\n### Compiling Tailwind\n\nAt the moment project contains package.json with all dependencies required to compile new CSS file. Tailwind configuration file is set to check all html, js and py files for Tailwind\'s classeses occurrences.\n\n```bash\nnpm install\nnpx tailwindcss -i styles.css -o src/unfold/static/unfold/css/styles.css --watch --minify\n\nnpm run tailwind:watch # run after each change in code\nnpm run tailwind:build # run once\n```\n\nSome components like datepickers, calendars or selectors in admin was not possible to style by overriding html templates so their default styles are overriden in **styles.css**.\n\nNone: most of the custom styles localted in style.css are created via `@apply some-tailwind-class;`.\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://unfoldadmin.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
