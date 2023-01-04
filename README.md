# Django Library Project (v2)

* Our user is the librarian, and the customers aren't able to login.

* Used the faker library for generating dummy data to make testing easier. Install with:<br/>
*python3 -m pip install faker*<br/>

## The process of each page ("..." = model name)
**`/`**            - Render the HTML page, used only for models navigation<br/>
**`/.../`**        - Get all avilable objects of the model, render in template, in template: display objects & actions (such as view & delete) in a table<br/>
**`/.../{pk}`**   - Get the specific model by it's id PK and pass the model's details to the template (the model object is passed automatically with the used generic view)<br/>
**`/.../create`**  - Create the required form in `Forms.py`, pass it to 'form' in the context<br/>
**`/.../delete`**  - Use as action only, figure out later...<br/>


## Good to Know
`LoginRequiredMixin`       inheritence in classes = Verifies that the current user is authenticated and logged in<br/>
`<int:pk>`                 in URL path (urls.py)  = Signifies the Primary Key of a modal in the URL, can be referred as "pk" in the view in this example<br/>
`default=None, blank=True` in a model             = Makes it None by default and there is no need to input it when creating the model<br/>
`auto_now_add` attribute   in DateField           = Assigns the current time to the field (datetime.date format) on creation (https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.DateField.auto_now_add) <br/>


## Avaialble Virtual Envoirements
.venv     = Virtual Envoirement for Windows<br/>
.venv-deb = Virtual Envoirement for Linux (https://www.javatpoint.com/django-virtual-environment-setup)
