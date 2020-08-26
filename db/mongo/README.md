# MongoDB
NoSQL!?! But how!!!

## Idea
Create an app that combines the best of an RDBMS and NoSQLDB to track orders in a restaurant as well as normalize menu options.
Create a chef and waiter page for this app.
Maybe add tables & seat #'s as well? idk.
Use in hypothetical scenario for fun :)

## Scenario
1. Place order from waitstaff
2. Cook it up as the chef
3. Bus it out to the correct table and chairs

### Design
**RDBMS holds**
- menu items
- toppings
- sides
- substitutions
- allergy info
- restaurant layout
- recipes

**NoSQL holds**
- order pipeline
  - what they want to eat
    - removals
    - substitutions
    - additions
    - sides
    - on-the-side
  - what they want to drink
    - strength
    - size
  - phase of order
    - cleaning
    - open
    - ordered
    - cooking
    - ready
    - served
      - re-ordered ^ back to top ^
    - check
    - closed
  - seat-to-order correlation
    - bill splitting
