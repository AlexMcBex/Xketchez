# Xketchez
*The luXury of sketches*

## Overview

What if I tell you that sketches can be art too? <br>
In Xketchez you can show your artistic talent in a matter of minutes. Pick the first pen and paper you can find, make a quick drawing, follow your instinct (you don't need to put too much effort in it tho...), share it with the world and watch it becoming part of a high-class, luxurious, snob and (not so) eXclusive art gallery. <br>
Describe to the world what powerful emotions you felt in all those 3 minutes of drawing. Browse other artists' masterpieces, grace them with a like and add them to your favorites list if you really like them.<br>
<br>
With Xketchez you can show the world that anything can be art (even sketches) and anyone can be an artist (even YOU).

---

## Technologies Used
- HTML5
- CSS
- Python
- Django
- Bulma
- Node JS
- AWS

---

## User Stories

- As a user I would like to share my sublime, low-effort art with the world
- As a user I would like to browse other people's art
- As a user I would like to like other people's art
- As a user I would like to tag as favorite other people's art
- As a user I would like to search art pieces by tag
- As a user I would like to leave a comment on art pieces
- As a user I would like to add other user as friends and follow them

---

## Route Tables

### Arts

| **URL** | **HTTP Verb** | **Action** |
|------|---------------|---------|
| /arts/  |    POST     | create     |
| /arts/:artId  |    GET      | show     |
| /arts/create|  GET |  new     |
| /arts/  |    GET      | index     |
| /arts/:artsId/edit | GET | edit |
| /arts/:artId |    PUT      | update     |
| /arts/:artId |    DELETE      | destroy     |

### Galleries
| **URL** | **HTTP Verb** | **Action** |
|------|---------------|---------|
| /galleries | GET | index   |
| /galleries/:galleryId |  GET | show   |
| /galleries/create|  GET |  new     |
| /galleries  |  POST |  create |
| /galleries/:teamId/edit | GET |  edit      |
| /galleries/:teamId/| PATCH/PUT |  update |
| /galleries/:teamId | DELETE  |  destroy |

### Profile
| **URL** | **HTTP Verb** | **Action** |
|------|---------------|---------|
| /profile | GET | index   |

### Auth
| **URL**          | **HTTP Verb**|**Action**|
|------------------|--------------|----------|
| /accounts/signup    | POST         | create  
| /accounts/login     | POST         | create       
| /accounts/logout    | DELETE       | destroy  



---

## Entity Relationship Diagram


![entityRelationshipDiagram](/img/ERD.png)

---

## Wireframes


### Art Index / Gallery Show

![Index of art pieces](/img/art-index.PNG)


### Art Show

![show a single art piece](/img/art-show.PNG)


### Galleries Index

![galleries index](/img/gallery-index.PNG)


### Art Create

![form to submit an art piece](/img/art-create.PNG)