# Diploma in Web Development – Milestone Project 3

## Mira Blog

### Project Overview
Mira is a responsive web blog and social platform that allows users to create, discover, search, filter and comment on blog posts. The platform is designed to be interactive, open and accessible to a wide range of end users and support a broad range of content.

The purpose of Mira is to provide a flexible space where blog content can be personal or opinion-based (i.e: food, travel, hobbies), and creative or lifestyle-focused interests. 
Each post is linked through filter tags, which helps users/visitors to search or filter the content they are interested in. Visitors/users can also explore recent posts from other users.

Mira is designed with a grid-looking visual, masonry-style layout, showing posts in different card heights to create a more dynamic browsing experience across different media. Views can be dynamically adapted to mobile, tablet and desktop, to create a consistent and accessible user experience on all devices.

---
### 1.00 Project formating
#### 1.01 Strategy Plane_User Goals
##### What visitors want to achieve ?
Mira Blog is designed for a range of users who want to discover and create blog content across different topics and interests.

Visitors want to:

- Browse a variety of blog posts from the landing page.
- Search and filter for posts using keywords or topic tags.
- Read full blog posts on particularly topics.
- View recent and explore-based content.
- Create their own blog posts after signing in.
- Add filter tags to their own posts so other users can discover them.
- Visitor could save or bookmark posts they want to return to.
- Visitor could Like and comment on blog posts.
- View their own profile and blog activity.
- Access the website across mobile, tablet, and desktop devices.

The website should presents the content discovery simple, visual, and accessible.

---
#### 1.02 Strategy Plane_Client Goals
##### What does mira want the website to achieve?
The main purpose of Mira is to create an inclusive hybrid social/blog platform.
The platform is not limited to any specific user or purpose, but a space for everyone to share and blog their own experiences. These experiences are filtered through tags, where individuals have similar mindset can like, follow and create an interaction.

The website should:
- Provide an open platform for users to share different contents.
- Allow blog posts to be personal, biase or lifestyle focused - i.e places for the best guinness experience in Dublin, places to hike in lake district etc..
- All posted blogs should be tagged, this encourage user to explore content through search and tag labels.
- Allow users to interact with the blog post via comment, like and follow.
- User should be able to create their own account to create blog posts.
- The website should allow the user to manage their own blog posts.
- The website should have a dynamic view across different small, mid and large screens.
- User should also able to share liked posts to other people.

---
#### 1.03 Strategy Plane_Developer and Business Goals
The strategy plane of a develpers aim is to create a full stack Django web application.

###### Developers aim:
- Build a Django project using a clear code and app structure.
- Use relational database to store,post,users,tags,comments,likes and save posts.
- Allow user to create,read,update & delete posts.
- Using tags to support the filter and search application.
- Web should be presentable across different screen size.

###### Business goals:
- Creating a social blog concept ideology.
- Encourage user to engage through interactive features, making content post and find related post via search and tag filters.
- Create platform that shares information, support collaboration, and community.
---
#### 1.04 Scope Plane_User Stories
The user stories has been added into github kanban board and is distrubuted using MoSCoW method to prioritise the important to less important features through Must Have, Could Have and Should Have.

See the [Kanban Board](https://github.com/users/JJYNG1023/projects/5) for lists of project user stories, divided into four sections of:
1. To do list  - lists of tasks marked in MoSCoW method
2. In progress - features currently working on
3. In review   - review how function perform in particular section
4. Done        - feature has been completed and marked done
5. Review with user story  - Final testing review against the user story

---   
#### 1.05 Skeleton Plane_Design Choices
The struction of Mira Blog is based on a hybrid blog/social platform, it should be a simple and accessible user journey allowing users to move between discovery, interaction, and creation features.

The skeleton plan would adapt across mobile, tablet and desktop devices to improve usability and accessibility.
On mobile view, the wireframe uses top and bottom navigation bar to support thumb navigation, allowing quick access to home, notification, user profile and create post.
The tablet view keeps the mobile first structure but expands the posts layout into a wider grid formate to make better use of the larger screen.
In the desktop view, the main navigation will be relocated to a left sidebar , allowing user to access main areas of the website faster.  

**Below are links to the wireframe layout, ERD and handwritten note in developing the skeleton plane structure. Please read in conjunction to the below comment:**
Click the link to see [handwritten notes]() on organising the app and pages
Click this link to see [Link_for_Wireframe_view](https://miro.com/app/board/uXjVHRk-oeo=/?share_link_id=370277439113)
Click this link to see [ERD](https://miro.com/app/board/uXjVHRHtjY0=/?share_link_id=138730307903)


##### Main navigation structure
The main structure planned for Mira contains:
1. Home/landing page
2. Search page
3. blog detail page
4. create post page
5. notification page
7. sign in page
8. register page
9. user profile page
10. bookmark page
11. about us and collaboration page

The ideology of the user flow circulation is: 
1. The user lands on the home page.
2. the user browses the Expore and recent blog posts.
3. the user searches for the topics their are interesed using search bar or filter tags.
4. the user click on a blog post to view the full post.
5. the user can share the post.
6. the user can signin or register an account to bookmark, like and comment on the posts.
7. only a signed in user can create a post and view their own profile.

---
#### 1.06 Styling
The visual style of Mira blog is designe to be minimalistic, clean and modern. The aim is to set out a clear page hierarchy for easy to read.
To do so, I have set up a default :root variable in CSS styling, this variable helps to refine text styles size, font and colours to make both css styple and webpage more unified and clear. 

``` 
:root {
    /* Colours */
    --primary-color: #ffeb33;
    --secondary-color: #212529;

    --icon-color-default: #fd7b41;
    --icon-color-interactive: #fd7b41;

    --main-title-color: #000000;
    --sub-title-color: #000000;
    --heading-1-color: #070707;
    --heading-2-color: #090909;
    --heading-3-color: #080808;
    --paragraph-color: #000000;
    --annotation-color: #939393;

    --background-color: #ffffff;
    --link-color: #0d6efd;
    --link-hover-color: #0a58ca;

    /* Font sizes */
    --font-size-xs: 0.7rem;
    --font-size-sm: 0.8rem;
    --font-size-base: 0.9rem;
    --font-size-md: 1rem;
    --font-size-lg: 1.1rem;
    --font-size-xl: 1.35rem;
    --font-size-xxl: 1.6rem;

    /* Font weights */
    --font-weight-regular: 400;
    --font-weight-medium: 500;
    --font-weight-bold: 600;

    /* Border radius */
    --radius-sm: 0.25rem;
    --radius-md: 0.5rem;
    --radius-pill: 999px;
}

```

##### Typography
```  /* Font sizes */
    --font-size-xs: 0.7rem;
    --font-size-sm: 0.8rem;
    --font-size-base: 0.9rem;
    --font-size-md: 1rem;
    --font-size-lg: 1.1rem;
    --font-size-xl: 1.35rem;
    --font-size-xxl: 1.6rem;

    /* Font weights */
    --font-weight-regular: 400;
    --font-weight-medium: 500;
    --font-weight-bold: 600;
```

The typography should be simple and readable across all devices.
In the variable style.css, I have set up a fix variable of font weight and font size to differentiate Title, Heading, Subheadings,Body text and Annotation text. 
Headings should be bold enough to create clear page hierarchy, while body text should remain easy to read.

##### Colour Scheme
The planned colour scheme will use a light and minimal design. Neutral colours will help the blog images and post content stand out.

Possible colour approach:
- Light background with dark text for readability
- Highlight colour for active buttons, selected tags, and important actions
- Grey buttons for annotation like edit and reply

At the moment, I have only used black and white for the colour scheme to maintain the readability and minimalistic. However, with the colour variation template I have set up, amending the colours can be easier and more efficent.

```    /* Colours */
    --primary-color: #000000;
    --secondary-color: #000000;

    --icon-color-default: #000000;
    --icon-color-interactive: #000000;

    --main-title-color: #000000;
    --sub-title-color: #000000;
    --heading-1-color: #070707;
    --heading-2-color: #090909;
    --heading-3-color: #080808;
    --paragraph-color: #000000;
    --annotation-color: #939393;

    --background-color: #ffffff;
    --link-color: #0d6efd;
    --link-hover-color: #0a58ca; 
```

##### Layout Style
As shown in the [Wireframe_view](https://miro.com/app/board/uXjVHRk-oeo=/?share_link_id=370277439113)

1. The landing page implements bootstraps grid card style layout, present each post with cover imagery, title and short 10word summary. This creates a more visual and interactive browsing experience and avoid overload of information.
2. The post detail page focuses on singular blog post, set out with bootstrap carousel, title, body of content, filter tags and comment section.
3. The rest of the webpage focuses on the same typology on same nav bar layout but different body of content.

---
#### 1.07 Surface Plane_Wireframes

As shown in the [Wireframe_view](https://miro.com/app/board/uXjVHRk-oeo=/?share_link_id=370277439113)
Wireframes mapped for mobile, tablet, and desktop screen sizes.

##### Mobile Wireframes
The mobile wireframes include:

- Landing Page
- Search Page
- Navigation Modal
- Notification Page (Notfication page is not been created, due to low priority)
- Create Post Page
- Blog Detail Page
- Expanded Blog Page with Comments
- My Profile Page
- Sign In & Sign Up Page
- About Us & Collaborate Page

The mobile view focuses on compact layout with top and bottom navigation to allow easier access to key actions.

##### Tablet Wireframes

The tablet wireframes include the same main pages as the mobile version allows three columns for displaying blog cards at landing page.

##### Desktop Wireframes
The desktop wireframes include a fixed left sidebar navigation panel. The main content area is wider which should be same as the tablet wireframe view.
The desktop layout improves navigation by keeping the sidebar visible while users browse the site.

---

### 2.00 Features
Current / Planned Features and relations are mapped out in [ERD](https://miro.com/app/board/uXjVHRHtjY0=/?share_link_id=138730307903)

##### Responsive Landing Page
The landing page displays a variaty of blog post cards in a visual grid layout. Each post card includes an image, title, and content preview.

##### Search Functionality
Users can search for blog posts using keywords to find content based on their interests.

##### Tag Filtering
Posts can include tags such as travel, food, hiking, nature, city explore, and landscape. Clicking a tag filter in the landing page filters the contents to that topic.

##### Blog Detail Page
Users can open a full blog post to read the content and view the post image, title, creator, date, and interactions.

##### User Authentication
Users can sign up and sign in to access account-based features like; bookmarked posts, notifications,users own blog posts and profile page.

##### Create Post
Signed-in users can create blog posts using a form with title, content, image, and tags.

##### Profile Page
Users can view their profile, posts, bookmarked posts, followers & following number count.

##### Likes & Comment
Authenticated sign in users can like and comment posts.

##### Bookmark Post
Signed-in users can bookmark posts.

##### Notifications
Users can view notifications related to post interactions.
(This function has not been developed as Notification falls in could have catagory. Due to time constraints it is not been added.)

##### About Us & Collaboration
The About Us page explains the purpose of Mira and includes a collaboration/contact section.

---

#### 2.01 HTML Features
HTML features planned include:
- Header navigation
- Main content sections
- Blog post cards (modified from boostrap)
- Forms for sign in & sign up (modified from Auth), create post, and collaboration
- Buttons for interactions
- Links for navigation
- Image elements with alt attributes
- Footer or bottom navigation for small to mid size screen views
  
---

#### 2.02 Bootstrap Features

Bootstrap is used to support responsive layout and faster front-end development and avoide over populated of css.
Bootstrap features planned include:
- Responsive grid system
- Containers and rows
- Navbar components
- Buttons
- Forms
- Cards
- Modal or offcanvas menu
- Responsive breakpoints for mobile, tablet, and desktop
- Bootstrap icons or Font Awesome icons

---

#### 2.03 CSS Features
Custom CSS are used to style the project beyond Bootstrap defaults.

CSS features planned include:
- Custom post, card & button styling
- Tag filter button styling
- Sidebar styling for desktop
- Bottom navigation styling for mobile
- Profile page layout
- Blog detail page layout
- Form styling
- Active states for buttons and filters
- Image sizing and object-fit styling

---

### 3. Technologies used
##### Languages
- HTML
- CSS
- JavaScript
- Python
- Django (Python based)

##### Frameworks and Libraries
- Django
- Bootstrap
- Font Awesome
- Python Packages 

##### Database
- PostgreSQL provided by code institute for local development
- Cloudinary for deployed static database

##### Tools
- GitHub
- VS Code / GitHub Codespaces
- Heroku
- Miro for wireframes
- Chrome DevTools
- Tool for testing_W3C HTML Validator 
- Tool for testing_W3C CSS Validator
- Tool for testing_Lighthouse

##### Python Packages
Python Packages are stored in the `requirements.txt`.

---

### 4. Testing
Testing are carried out throughout the project development against the user story to make sure the website works correctly and provides a good user interface.

##### Testing during development
Test includes:
- Manual functionality testing
- User story testing
On each cycle of completed user story a manual user testing is committed to minise errors before moving onto the next user story function.

##### Testing after development
Test includes:

- Manual functionality testing
- User story testing
- HTML validation
- CSS validation
- Python code validation
- Responsive testing
- Browser testing
- Deployment testing

#### 4.01 Testing Must-Have stories from UX section of README.md
| User Story | Test | Expected Result | Result |
|---|---|---|---|
|As a site visitor, I can view a selection of blog posts on the landing page so that I can discover different types of content when I first enter the website. | Open the landing page | landing page displays multiple Blog post cards | Pass |
| As a site visitor, I can use the search bar to search for blog posts so that I can quickly find content that matches my interests. | Enter a search term in the search bar, relevant blog posts are displayed and allowing user to select| Relevant posts are displayed | Pass |
| s a site visitor, I can click on filter tags so that I can view blog posts related to topics I am interested in. | Filter tags are displayed on the top of landing page, click a tag filter button to show relevent posts | Posts with the selected tag are shown | Pass |
| As a site visitor, I can click on a blog post card to open the full blog page so that I can read the full content and view all related post details. | Click a blog card | Blog detail page opens | Pass |
| As a site visitor, I can navigate the website easily across different screen sizes so that I can use the platform on mobile, tablet, and desktop devices. | Test on small, mid and large screen view size | Webpage should adapt the different screen size | Pass |
| As a new user, I can create an account so that I can access personal features such as creating posts, saving posts, and managing my profile. | Creating a new user account | Account is created | Pass |
| As a signed-in user, I can view my profile | Open profile page | User profile and posts are shown | Pass |
| As a signed-in user, I can create a blog post and add filter tags to the created posts| Add filter tags to the create post form and submit | New post appears on the website along with filter function | Pass |
| As a user, I can sign in and sign out when click the sign in / sign out button | Side nav bar displays sign in. Once signed in, a sign out button/text will appear | User can sign in and sign out | Pass |
| As a site visitor, I can view the About Us page so that I can understand the purpose of Mira and what the platform offers. | The about us should open a seperate html page to display about us information | about us information is visible | Pass |
| As a signed-in user, I can comment on a blog post so that I can interact with the creator and other users. | Blog detail page includes a comment input field and user can submit a comment when signed in | After user sign in, user can comment on posts | Pass |
| As a signed-in user, I can edit or delete my own blog posts so that I can manage the content I have published. | Users can edit, delete their own posts. | Edit options allows the user to update the title, content,image and filter tags. While the detele button removes the posts | Pass |
---

#### 4.02 Functionality Test
| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Navigation links | Click each navigation link | Correct page opens | Pass with condition |
| Search bar | Search for a keyword | Matching blog posts appear | Pass |
| Tag filters | Click a tag | Blog feed filters by selected tag | Pass |
| Blog cards | Click a post card | Blog detail page opens | Pass |
| Sign up form | Submit valid details | User account is created | Pass |
| Sign in form | Submit valid details | User logs in successfully | Pass|
| Create post form | Add title, content, image, and tags | Post is created | Pass |
| Comment form | Submit a comment | Comment appears under post | Pass |
| Like button | Click like icon | Post like status updates | Pass |
| Save button | Click bookmark icon | Post is saved to profile | Pass |
| Profile tabs | Click Blogs, Saved, Likes | Correct content is displayed | Failed, Revised the css so the profile tab is visable on large screen views |
| Collaborate form | Submit name, email, and message | Confirmation is shown | Pass |

---
#### 4.03 Testing with HTML Validator
[HTML landing page](/validator/html%20validator/landing%20page.png)
Landing page fix
1. ``` <form class="mira-search-form" action="{% url 'search_posts' %}" role="search" method="GET">
                    <input
                        class="form-control mira-search-input"
                        type="text"
                        placeholder="Search"
                        readonly>
      </form> ```

2. Removed additional ``` </div> ``` ending
3. ``` <div class="offcanvas offcanvas-start mira-nav-modal" tabindex="-1" id="miraNavMenu" aria-labelledby="miraNavMenuLabel" role="dialog"> ```

Lists of pages below has minor issues with h2-h6 element, no serouse error issues: 
[HTML Profile page](/validator/html%20validator/Profile%20page.png)
[HTML My_blog page](/validator/html%20validator/My_blog%20page.png)
[HTML Create_blog page](/validator/html%20validator/My_blog%20page.png)
HTML bookmarked page - minor issues with h2-h6 element,
HTML post_detail page- No error or issues

#### 4.04 Testing with CSS Validator
[CSS Validator](/validator/css%20validator/css.png)
The css only has one error with:
```.carousel-control-prev,
.carousel-control-next {
    filter: 1;
} ```
This was added before to make the boostrap carousel more stand out from the background, however it is not needed now and code will be deleted to remove error.

#### 4.05 Testing with Light House


### 5. Deployment
The project will be saved on github and deployed using Heroku.

#### 5.01 Deployment Progress Completed
The following are the steps taken to deploy the current project:
1. Created the GitHub repository named `Project_3_Mira_Blog`
2. Set up the Python development environment
3. Added a `.gitignore` file
4. Added SQL database configuration
5. Added Cloudinary database configuration
6. Updated `env.py` and `settings.py`
7. Installed required plugins using `requirements.txt`
8. Created the main Django app called `mira_blog`
9. Linked the GitHub repository to Heroku
10. Added the secret key and SQL database key to Heroku Config Vars
11. Make migration on changes in models.py and creation of new apps.
12. Temporarily added `DISABLE_COLLECTSTATIC=1` on Heroku
13. Committed all changes to GitHub
14. Remove the `DISABLE_COLLECTSTATIC=1` on Heroku
15. Re-deploy project on Heroku

#### 5.02 How to run this project locally
To clone this project from GitHub

1. Click the attached link to the Project GitHub Repository
2. Under the repository name, click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the respository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type "git clone", and then paste the URL you copied in step 3.
Git Clone: https://github.com/JJYNG1023/Project_3_Mira_Blog.git
Press Enter. Your local clone will be created.


### 6. Credit

#### 6.01 Content

The text, image, links and other data in the database was sourced from various local websites including but not limited to:

TripAdviser 


#### 6.02 Media



#### 6.03 Code

Credit: bootstrap template code for : 
- Carousel
- 

Credit: Code institute lession on Django framework:
-
-

Credit: CHATGPT on bug fixing:

Credit: Visual Studio Code's built-in AI features are powered by GitHub Copilot

#### 6.04 Acknowledgements
