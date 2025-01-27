![Project banner](/Media/HABIT%20TRACKER%20(1).png)

HABIT TRACKER is for the people that are eager to inplement habits into there day to day activities. This App will keep track and help motivate people to remain steadfast developing these habits into peoples lives.

# What the website looks like



# User Stories

As a user, I want to set specific habits I want to develop, so I can track my progress toward achieving them.

As a user, I want to set a schedule for each habit so I can follow it consistently.

As a user, I want to mark certain habits as high priority, so I can focus on the most important ones.

As a user, I want to set big goals connected to my habits, so I can see how my daily progress helps me achieve them.

# User Design

**WIREFRAMES**

I used Figma to create a mockup of the websites front page from the perspective of a desktop and mobile. These wireframes are not going to be fully implemented into the websites design although the asthetic will be very simular apart from the colour scheme.

![Wirframes](/Media/Habit%20tracker.png)
![Wirframes](/Media/habit%20tracks%20phone.png)

**COLOUR SCHEME**

This colour pallete Shows the chosen colours that will be shown through out this project. The colour pallete is in order from most seen to least.

![colour pallete](/Media/color%20pallete.png)

**fonts**

I have chosen the "Russo One" font for my header to make it pop out and very noticable to cause the user to remember the name. While the rest of the projects text will be using the "Faustina" Font.

Header: Russo One

![Fonts](/Media/Font%20header.png)

Body: Faustina

![Fonts](/Media/Rest%20font.png)


# App Implementations track record via Kanban board on GitHub Projects

For keeping track of implementations, I am using the Kanban board on GitHub Projects to give efficient management to the development of the project. view the [project board here](https://github.com/users/WhatTheyOnn/projects/2)

The kanban board helped ensure continuous progress and adaptability throughout the project. The board has different collums for each task to identify where they was:

![projectboard](/Media/project%20board.png)


**To Do:** In this column, we listed tasks and user stories that were identified but not yet prioritized for development.

**In Progress:** This column tracked tasks that were actively being worked on.
It helped to show ongoing development efforts and keep focus on current objectives.

**Complete:** Tasks that were successfully finished were moved to this section for review or testing.
This column showed the progress made and served as a record of what had been accomplished.

**Future Implementation:** In this column, we kept potential features and ideas for future releases.
It allowed for long-term planning while keeping immediate priorities clear.




# Interface 

So far the website mimics the majority of the wire frames. 

There are 2 different homepages that depend on the user authentication status.

If user is not authenticated:


![Homepage](/WebsiteMedia/Home%20page.png)


If user is authenticated: 


![Homepage](/WebsiteMedia/home%20page%20when%20logged%20in.png)


A small change that will drastically change the overall functionality of the website according to the user.

If the user is not authenticated but tries to add/edit a habit, he will be sent straight to the login page.



![Loginpage](/WebsiteMedia/Log%20in%20page.png)


For this to be the case, i edited the index code in view.py to allow users that are not authenticated to be on the home page but not able to use features that are strictly for logged in users.


![Code](/WebsiteMedia/Home%20page%20code.png)


I also wanted the visibility of the loggedin/loggedout to depend on if you're authenticated or not. And i added an interaction to users that are logged in with their specific username added to maintain good implementations into the app.

This was done via the list.html code with a simple if/else command.

![code](/WebsiteMedia/home%20page%20code%202.png)


However if the user wants to log in but inputs an incorrect username/password, they will be shown a flash message showing their error.


![loginflashmessage](/WebsiteMedia/Log%20in%20page%20when%20incorrect.png)


This was also added to the register form if they incorrectly filled out the inputs.

![Registerflashmessage](/WebsiteMedia/sign%20up%20with%20error%20message.png)


Or if they enter the form correctly they will be sent back to the login page with a flash message, showing their sign up was successful also addressing their username specifically

![Registerflashmessage](/WebsiteMedia/login%20auth.png)

This implementation was added using the in place django setup.


![flashmessagecode](/WebsiteMedia/flash%20messages%20code%201.png)
![flashmessagecode](/WebsiteMedia/flash%20messsages%20code%202.png)
![flashmessagecode](/WebsiteMedia/login%20flashmessage%20code.png)
![flashmessagecode](/WebsiteMedia/register%20flash%20message%20code.png)

When selecting the update button on a specific habit you will be taken to this page, which is coded in the Habit_update.html


![Update](/WebsiteMedia/Update%20section.png)

The update button will update whatever you had edited and will be seen in the homepage once you are redirected back after clicking the update button. but if you select the back home button on the top left all updates selected will be canceled.


When selecting the delete button you will be taken to the this page giving you 2 options: confirm or cancel

![delete](/WebsiteMedia/Delete%20section.png)

selecting either one of these will take you back to the home page, but depending on what you had picked, the habit will or will not be there anymore.



# Testing

To run the python test i used this command in the terminal "python manage.py test"

![Pythontest](/Media/tesst%202%201.png)

I used this code to test:

Model Creation: This test_habit_creation method checks if a Habit instance can be created and if its title is set correctly

String Representation: This test_habit_str method verifies that the str method of the Habit model returns the correct string representation.

Default Values: This test_habit_default_values method checks that the default values for completed and created fields are set correctly.

The result:

![Pythontest](/Media/tests%202.png)