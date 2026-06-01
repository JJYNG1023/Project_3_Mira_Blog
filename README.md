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

#### Mobile Wireframes
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

# 2.02 Bootstrap Features

Bootstrap will be used to support responsive layout and faster front-end development.

Bootstrap features planned include:

- Responsive grid system
- Containers and rows
- Navbar components
- Buttons
- Forms
- Cards
- Modal or offcanvas menu
- Utility classes for spacing
- Responsive breakpoints for mobile, tablet, and desktop
- Bootstrap icons or Font Awesome icons if needed

---

# 2.03 CSS Features

Custom CSS will be used to style the project beyond Bootstrap defaults.

CSS features planned include:

- Custom post card styling
- Masonry-style grid layout
- Responsive media queries
- Custom button styling
- Tag filter button styling
- Sidebar styling for desktop
- Bottom navigation styling for mobile
- Profile page layout
- Blog detail page layout
- Form styling
- Hover effects
- Active states for buttons and filters
- Image sizing and object-fit styling

---

3. Technologies used
4. Testing
4.01 Testing client stories from UX section of README.md
4.02 Functionality Test
4.03 Testing with HTML Validator
4.04 Testing with CSS Validator
5. Deployment
5.01 How to run this project locally


### WireFrame View
[Link_for_Wireframe_view](https://miro.com/app/board/uXjVHRk-oeo=/?share_link_id=370277439113)

### ERD
[Link_for_ERD](https://miro.com/app/board/uXjVHRHtjY0=/?share_link_id=138730307903)


