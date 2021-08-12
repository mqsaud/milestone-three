# Milestone Three Project - Soup & Soft
Soup & Soft is a soup and drink shop sells a variety of soup and drinks. The target audience of this website is soup lovers who want to prepare soup and beverages themselves. Everyone is welcome.

Recipes are visible to all visitors. Only registered users can upload recipes and can edit their own recipes.
Registration is open to all visitors.

To visit the website please click [Here](https://milestone-three-pro.herokuapp.com/)

![Responsive-Site](static/images/site-responsive.jpg)

## Contents

- [**User Experience (UX)**](<#user-experience-(ux)>)

  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [Design](#design)
  - [Wireframes](#wireframes)

- [**Features**](#features)

  - [Existing Features](#features)

- [**Technologies**](#technologies-used)

  - [Languages Used](#technologies-used)
  - [Frameworks, Libraries and Programs Used](#technologies-used)

- [**Testing**](#testing)

- [**Deployment**](#deployment)

- [**Credits**](#credits)

## User Experience (UX)

### Project Goals
- Create a website to inspire users to share their favourite recipes.
- Create and implement navigation throughout the site to help users to register,     login and manage their posts/recipes.
- Implement  CRUD (create, read, update and delete) functionalities for users recipes.
- Implement following technologies:  
CSS, Flask, HTML, JavaScript, MongoDB and Python

## User Stories

### User Goals:
#### New User Goals:  
As a new user, I want to achieve the following goals.  
a- I want to be able to view all shared recipes.    
b- I want to be able to register on the website.  
c- I want to be able to share/upload my recipes.  
d- I want to be able to edit/delete my recipes.  
### Returning User Goals:  
a- As a returning user, I want to be able to edit/update my recipes posted on the website.  
b- As a returning user, I want to be able to delete my recipes posted on the website.  
### Site Owner User Goals:  
a- As the site owner, I want to share the recipes uploaded on this website.  
b- As the site owner, I want to attract the audience with the nice and attractive design of the website.  

### Design  
* The design of this project is simple.  
Materializecss.com framework was used to build this project website.  

### Colors  
* I used followig colours including text colors.  
![color used to build websitr](static/images/color-used.jpg)  

### Typography  
- I used the operating system default font to enhance the compatibility.  

### Wireframe  
- To view the project wireframe please click [Here](https://github.com/mqsaud/milestone-three/blob/main/Soup%26Soft%20Cafe.pdf)  

## Features

### Existing Features : 

- **Navigation**:  
  Standard Materialize based navigation bar was added with a clear name of the company on the left in desktop view and centred in mobile view.

- **Footer**:  
The footer includes the email address and Social link icons.

- **Home Page**:  
The landing page contains a separate beautiful hero image for each device type. The navbar offers the user to register or login

- **Profile**:  
Once logged in, the user will transfer onto the profile page. Here the user will be able to edit or delete their uploaded recipes. 

- **Flash messages**  
Customized flash messages will appear for successful and non-successful registration, successful login and logout, successful update, successful edit and added recipes.

- **Add / Edit recipe** :   
Once the user logged in, users can see the option to Add or Edit the recipe. On the navbar, they will see the option "Add Recipe". Once clicked, they will fill the relevant information in the form, and by clicking " Add Recipe", the recipe will upload to the website and be available for viewing to all visitors. Any registered user can edit or delete only their own uploaded recipe.

- **Delete**:  
If a user wants to delete a recipe, they will have to login first. There is a  defensive check by using a pop-up modal, asking them to think one more time before deleting the recipe.

- **Logout**:  
If the user clicks "Logout", they will be redirected to the "Log In" page, as they might need to login again.

- **Search**:  
As the site grows, there will be more recipes; therefore, search functionality has been added to search the recipes.

**Database skeleton**

- The skeleton of my database is as follows : 

<img src="static/images/data-base.jpg" width=100% height=100%>

- **categories** : 

    category_name

- **recipes** : 

    recipe_name

    category_name

    img_url

    ingredients

    method --> Cooking Procedure

    veg_no_veg --> Is the recipe vegetarian or non-vegetarian.

    added_by

- **users** :

    username

    password
    
**Security**

- The website uses [Werkzeug's](https://werkzeug.palletsprojects.com/en/1.0.x/) password protection system.  Werkzeug hashes the password entered by the user, converts the password into another string and then it is salted (additional data added). The hash of the password is stored in the database. This makes the password very tough to crack.

- Database configurations, username, password/"secret key" are stored in a separate file, and gitpod's .gitignore file was used to prevent this file from uploading to GitHub.

#### [Back to Contents](#contents)

---

## Technologies Used
- Following languages and frameworks were used to build the website

### Languages

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/v1619744963/html5_rjkhoe.png) [HTML5](https://en.wikipedia.org/wiki/HTML5)
>
![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/v1619744731/css_mvqiie.png) [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
>
![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/v1619744731/js_fveoqo.png) [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/pictures/logos/python_mbbj4o.png) [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs:

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60,h_50/v1624909475/pictures/logos/Flask_h8fuus.png) [Flask](https://fontawesome.com/)

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60,h_60/v1624909475/pictures/logos/MongoDB_lintsi.png) [MongoDB](https://www.mongodb.com/) 

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60,h_50/v1624909475/pictures/logos/gitpod_kbbawd.png) [Gitpod](https://www.gitpod.io/) 

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60,h_50/v1624909475/pictures/logos/Materialize_uzrnyu.png) [Materialize](https://materializecss.com/about.html) 

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/v1619745480/pictures/logos/font_awesome_logo_djde4p.png) [Font Awesome](https://fontawesome.com/) 

![Image](https://res.cloudinary.com/docyuifc9/image/upload/c_scale,w_60/v1619745480/pictures/logos/balsamiq_wireframes_logo_eieeug.png) [Balsamiq](https://balsamiq.com/) 

#### [Back to Contents](#contents)

---

## Testing

### Code validity

**PEP8 Compliant:**

   I have used [PEP8](http://pep8online.com/) to check my mst.py files complied with the PEP8 requirements. The results was no error
   ![pep8](static/images/pep8.jpg)

