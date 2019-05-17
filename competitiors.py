""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run
import random

"""
This template is written by Amit Upreti
This is avery good strategy to steal followers from your comepetitors


"""




#new changes has been made inside this box for proxy setup
#########################################################################################################################################

# from proxy_extension import create_proxy_extension
# #this in case your proxy has username and password
# proxy = 'lum-customer-hl_e5a0e1f6-zone-usa_instagram-ip-38.131.151.4:7j6kam84o78a@zproxy.lum-superproxy.io:22225'
# proxy_chrome_extension = create_proxy_extension(proxy)

# login credentials
insta_username = 'user'
insta_password = 'pass'

# get a session!
# set headless_browser=True to run InstaPy in the background. You can set Up proxy here.
session = InstaPy(username=insta_username, 
                  password=insta_password,
                  headless_browser = True,
                #   proxy_address='202.79.34.115', #uncomment there if your proxy has no username and password
                #   proxy_port=8080   #uncomment there if your proxy has no username and password

                #  proxy_chrome_extension=proxy_chrome_extension #remove this line if your proxy has no username and password
                  )

# let's go! :>
##########################################################################################################################################






with smart_run(session):
    """ Activity flow """
    # general settings
    '''
        This is where you define the max and min followers and following the account should have
        potency ratio helps you determine whether the account we are trying to interact with is good fit for us. You can calculate it with

            potency_ratio = followers count / following count 
        "None" means the bot will not filter by that parametetr Here i have set max_post to none. So the bot wont care if the account has zillion posts or zero posts

    '''
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=0.4,
                                    delimit_by_numbers=True,
                                    max_followers=100000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=10,
                                    max_posts=None)


    '''
    keywords that the username should not contain. This is useful   if you want the bot to not follow certain kinds of people
    '''
    session.set_dont_include([
                            'sincere',
                            'zahara', 
                            'swim', 
                            'bikini', 
                            'company', 
                            'apparel', 
                            'clothing', 
                            'official',
                            'swimwear', 
                            'wholesale', 
                            'manufacturer']) 



    '''
    Here you will define the tags or words that we should avoid while engaging with somebody's post.
    Use this section to avoid bot to comment on unrelavant users. This is very useful to get to right audience
    '''
    session.set_dont_like(['rip', 
                            'R.I.P.', 
                            'rest', 
                            'cancer', 
                            'sexy', 
                            'boobs', 
                            'nude', 
                            'rape', 
                            'trump', 
                            'abortion',
                            'collegebabes', 
                            'sexyselfie', 
                            'wholesale', 
                            'manufacturer'
                            ])



    # activity

    '''
    It defines how many posts of a user should our bot interact with. 
    Similarly percentage is for descision whether the bot should engage or not

    '''
    session.set_user_interact(amount=3, randomize=False, percentage=100, media='Photo')



    '''
    Here we define the percentage  whether the bot should follow,like the account or not
    '''
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=100)
    session.set_action_delays(enabled=True, like=5,comment=5,follow=5)


    #setting comments. Please include as much comments you can


    session.set_comments([
                            u'I am representing Nepal in Miss World Now. Help me stand out:heart:',

                            u'Help me win the Miss Popular Award in Miss World 2019:heart:',

                            u'please help me qualify for the Miss WORLD 2019 by following me .',
                            
                                ],
                        media='Photo')





    '''
    This is section where you make sure you account doesnot get blocked.
    It helps the bot to take rest after certain limits . For example- after certain amount of likes or follows or comments
        Here
            peak_likes=(50, 1000) -> 50 is hourly like limit and 1000 is daily like limit
            peak_comments=(31, 600) -> 21 is hourly comment limit and 500 is daily comment limit
            peak_follows=(50, None) -> 50 is houry follow limit and None means that there is no daily follow limit

        Please use it wisely and dont be greedy. I am not reponsible if you try to do high number of follows ,comments or likes per day.
        This will run 24/7 so dont worry and choose small numbers
    '''
    session.set_quota_supervisor(enabled=True,
            sleep_after=["likes", "follows"],
            sleepyhead=True, stochastic_flow=True,
            notify_me=False,
            peak_likes=(None, 800),
            peak_comments=(50, None),
            peak_follows=(30, 600))


    #percentage for whether the bot should comment on the post or not
    session.set_do_comment(enabled=True, percentage=60)



    competitors = ['nepaltiktok','trishala__official','trending_nepal','troller343','nepalitiktok_official','']
    while True:

        random.shuffle(competitors)


        '''if you have lesss number of competitors account or want to use few accounts in each session edit the number below.
        For example
            my_competitors = competitors[:5] The bot will go after 5 accounts in each session
            my_competitors = competitors     The bot will go after all the accounts in each session
        '''

        my_competitors = competitors[:2]
        
        #here is where you put the instagram accounts of your followers
        #add many competitors as you want . 
        #here amount means how many followers to go after of each competitors
        session.interact_user_followers(my_competitors, amount=100, randomize=True)
        session.follow_by_tags(['nepal', 'nepali','nepalikto','kathmandu','tiktoknepal'], amount=100, interact=True)



        '''
        Here we unfollow users that we followed earlier by our bot. It wont unfollow people that you have followed manually

        As we target mainly active accounts, I use two unfollow methods. 
        The first will unfollow everyone who did not follow back within 12h.
        The second one will unfollow the followers within 24h.


        Bonus Tip: If you want to unfollow people who havenot followed you back.
        change InstapyFollowed=(True,"nonfollowers") to InstapyFollowed=(True,"nonfollowers")

            example:
                session.unfollow_users(amount=500, InstapyFollowed=(False, "nonfollowers"),
                                style="FIFO",
                                unfollow_after=12 * 60 * 60, sleep_delay=551)
        '''
        session.unfollow_users(amount=200, InstapyFollowed=(True, "nonfollowers"),
                                style="FIFO",
                                unfollow_after=2* 12 * 60 * 60, sleep_delay=551)


        session.unfollow_users(amount=600, InstapyFollowed=(True, "all"),
                                style="FIFO", unfollow_after=3 * 24 * 60 * 60,
                                sleep_delay=551)
        