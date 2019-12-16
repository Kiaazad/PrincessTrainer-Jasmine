# Variable naming patterns
Here are the patterns we use for naming.The priority goes to them in this order:

### Characters
Character get their name all lowercase, they are the top priority and anything else with the same name as a character gets a different name.
Note: this is different from the Character class that handles dialogue.
```python
default abdul = unit(
    name = _("Abdul"),
    dir = "char/abdul",
    )
```
### VN characters and images
For the script we use 3 first letters of a character's name.


### Items
Items get their name in lower case as well since it's rare for a character and item to get the same exact name.
```python
default wood = item(
    _("Wood"),
    )
```
### Spells
Spells follow the same format as items as well.

# Label naming patterns

# Screen naming patterns

# Styles naming

Note: variables inside `_()` will be available for translation.