Last login: Fri Mar 27 12:43:46 on ttys001
/Users/praghav/.zshrc:8: unmatched `
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	copy.json	hash.text	pattern.py	sample.text	web_scrapper.py
praghav@6622 Chef % pwd
/Users/praghav/Desktop/Project/Chef/Chef
praghav@6622 Chef % 
praghav@6622 Chef % 
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"
Traceback (most recent call last):
  File "URL_Access.py", line 35, in <module>
    main()
  File "URL_Access.py", line 32, in main
    filtering(git_url)  
  File "URL_Access.py", line 15, in filtering
    wfile.write(a.getcode())
TypeError: write() argument must be str, not int
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	copy.json	file.text	hash.text	pattern.py	sample.text	web_scrapper.py
praghav@6622 Chef % rm file.text 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	copy.json	hash.text	pattern.py	sample.text	web_scrapper.py
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	copy.json	file.text	hash.text	pattern.py	sample.text	web_scrapper.py
praghav@6622 Chef % vim URL_Access.py 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	sample.text	web_scrapper.py
praghav@6622 Chef % vim sample.text  
praghav@6622 Chef % vim sample.text 
praghav@6622 Chef % rm sample.text 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim file
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim file.text 
praghav@6622 Chef % vim file.text
praghav@6622 Chef % clear















praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim URL_Access.py 
praghav@6622 Chef % vim URL_Access.py
praghav@6622 Chef % ls               
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim U
praghav@6622 Chef % vim URL_Access.py 
praghav@6622 Chef % 
praghav@6622 Chef % vim URL_Access.py
praghav@6622 Chef % clear










































praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"
Traceback (most recent call last):
  File "URL_Access.py", line 38, in <module>
    main()
  File "URL_Access.py", line 35, in main
    filtering(git_url)  
  File "URL_Access.py", line 21, in filtering
    data1 = json.load(json_file)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim file
praghav@6622 Chef % vim file.text 
praghav@6622 Chef % ls  
Chef_hashes.csv	URL_Access.py	file.text	file_final.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim file_final.text 
praghav@6622 Chef % rm file_final.text 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim web_scrapper.py 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim file.text 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % vim URL_Access.py 
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"
Traceback (most recent call last):
  File "URL_Access.py", line 38, in <module>
    main()
  File "URL_Access.py", line 35, in main
    filtering(git_url)  
  File "URL_Access.py", line 20, in filtering
    with open("/Users/praghav/Desktop/Project/Chef/Chef/file_final.text") as json_file:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/praghav/Desktop/Project/Chef/Chef/file_final.text'
praghav@6622 Chef % vim URL_Access.py                                                                         
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"
Traceback (most recent call last):
  File "URL_Access.py", line 38, in <module>
    main()
  File "URL_Access.py", line 35, in main
    filtering(git_url)  
  File "URL_Access.py", line 21, in filtering
    data1 = json.load(json_file)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/json/decoder.py", line 340, in decode
    raise JSONDecodeError("Extra data", s, end)
json.decoder.JSONDecodeError: Extra data: line 1 column 13162 (char 13161)
praghav@6622 Chef % vim URL_Access.py                                                                         
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"
{'id': 26099105232, 'auth_username': 'ngaffey', 'prefix': '', 'first_name': 'Nuala', 'middle_name': '', 'last_name': 'Gaffey', 'nickname': '', 'suffix': '', 'pronouns': 'she/her', 'gender': '', 'email': 'ngaffey@etsy.com', 'enabled': 1, 'workday_employee_id': '1317', 'department_id': 0, 'employee_type': 'Regular', 'join_date': 1433808000, 'fulltime_date': 0, 'termination_date': 0, 'birthday': '', 'manager_auth_username': 'cclark', 'title': 'Senior Security Engineer II', 'team': 'Infrastructure and Operations', 'office': 'Brooklyn, NY', 'desk_phone': '', 'cell_phone': '6314088045', 'home_phone': '', 'skype': '', 'pager_email': 'ngaffey@etsy.com', 'irc_nick': 'ngaffey', 'slack_nick': 'ngaffey', 'slack_id': 'U27F4A3F0', 'user_id': 67678667, 'login_name': 'nualagaffey', 'shop_name': '', 'twitter': '', 'github': 'nuala33', 'linkedin': '', 'org': 'Cost of Revenue (FSLI)', 'dept': 'Technology - Security', 'group': '', 'phonetic_name': 'Noo-la', 'location': '', 'zendesk_id': 0, 'full_name': 'Nuala Gaffey', 'name': 'Nuala Gaffey', 'short_name': 'Nuala', 'is_manager': True, 'department': 'Infrastructure and Operations', 'avatar': 'https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0', 'badges': [{'id': 389928128051, 'badge_name': 'Local Roots NYC', 'badge_alt': 'This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ', 'link_url': '', 'image_url': 'https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209', 'datafeed_url': None, 'flavor_text': 'Alexa, how do I cook kohlrabi?', 'is_deleted': False, 'create_date': 1535043147, 'update_date': 1541701591}, {'id': 618614020664, 'badge_name': 'Eng Onboarding Lightning Talks', 'badge_alt': 'Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks', 'link_url': '', 'image_url': 'https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1569358386, 'update_date': 1569572097}, {'id': 588523834498, 'badge_name': 'Onboarding Helper', 'badge_alt': 'Thank you for helping during our on-boarding session. We appreciate you.', 'link_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'image_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'datafeed_url': None, 'flavor_text': 'You are a unicorn WOOP WOOP', 'is_deleted': False, 'create_date': 1565717083, 'update_date': 1569953561}, {'id': 39501666387, 'badge_name': 'I visited the Dublin office', 'badge_alt': 'For all the wonderful visitors to the Dublin office', 'link_url': '', 'image_url': 'https://i.imgur.com/QjpsuPK.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1455897522, 'update_date': 1556032479}, {'id': 205062567454, 'badge_name': 'B.A. is for Bad Ass', 'badge_alt': 'No time for B.S. (for Engineers with B.A. Degrees)', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1507926840, 'update_date': 1563393681}, {'id': 49750688293, 'badge_name': 'I see, you see, your yu-bi-key!', 'badge_alt': 'I&#39;ve seen your yubikey ;) They saw your yubikey ;) ', 'link_url': 'https://github.com/pallotron/yubiswitch', 'image_url': 'https://i.imgur.com/HExbKU6.png', 'datafeed_url': None, 'flavor_text': 'mmmm, keys. ', 'is_deleted': False, 'create_date': 1471533753, 'update_date': 1551114177}, {'id': 105074684569, 'badge_name': 'forever VIB', 'badge_alt': 'always buying from sephora just for the samples', 'link_url': '', 'image_url': 'http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357', 'datafeed_url': None, 'flavor_text': 'is it glamglow?', 'is_deleted': False, 'create_date': 1487197073, 'update_date': 1487197073}, {'id': 415079814924, 'badge_name': 'I have accepted Peanut Butter and Pickle into my life', 'badge_alt': 'Everything a grown adult needs for health and vitality', 'link_url': '', 'image_url': 'https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg', 'datafeed_url': None, 'flavor_text': '&quot;Ambrosia&quot; -- Shayne Barr', 'is_deleted': False, 'create_date': 1540850069, 'update_date': 1540850194}, {'id': 210882889226, 'badge_name': 'Atonal Music Lovers', 'badge_alt': 'maybe not, but we tried!', 'link_url': '', 'image_url': 'http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1508965668, 'update_date': 1508965668}, {'id': 331242931409, 'badge_name': 'Coda as Craft', 'badge_alt': 'You&#39;ve sung with Etsy&#39;s a capella group!', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1527108861, 'update_date': 1527108861}, {'id': 319226515931, 'badge_name': 'Certified ScrumMaster ', 'badge_alt': 'You completed the CSM training! ', 'link_url': 'http://scrumguides.org/scrum-guide.html', 'image_url': 'http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1525709146, 'update_date': 1572026189}, {'id': 35378054248, 'badge_name': 'Security Champion', 'badge_alt': 'You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.', 'link_url': '', 'image_url': 'https://i.imgur.com/AHXwccN.png', 'datafeed_url': None, 'flavor_text': '?alertword', 'is_deleted': False, 'create_date': 1447398334, 'update_date': 1570474992}, {'id': 47054459247, 'badge_name': 'Order of Saint Theodore of Feckton', 'badge_alt': 'I have been to Dublin and survived the Engineering Teams.', 'link_url': '', 'image_url': 'https://i.imgur.com/269SaI1.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465813717, 'update_date': 1563277966}, {'id': 35813106870, 'badge_name': 'ELK Wrangler', 'badge_alt': 'For those who have helped wrangle the ELK cluster', 'link_url': '', 'image_url': 'https://i.imgur.com/9l0i7mj.png', 'datafeed_url': None, 'flavor_text': 'A Møøse once bit my sister... No realli!', 'is_deleted': False, 'create_date': 1448475304, 'update_date': 1498240351}, {'id': 64300114379, 'badge_name': 'Golden SOX', 'badge_alt': 'This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX', 'link_url': '', 'image_url': 'https://i.imgur.com/LX2CQWk.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': True, 'create_date': 1478875468, 'update_date': 1570568682}, {'id': 34566765264, 'badge_name': 'I&#39;ve done doubles dev!', 'badge_alt': 'You&#39;ve done doubles! ', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg', 'datafeed_url': None, 'flavor_text': 'DD 4 EVA', 'is_deleted': False, 'create_date': 1445969385, 'update_date': 1558027395}, {'id': 38011401266, 'badge_name': 'SOX', 'badge_alt': 'For service above and beyond the call of duty in the line of SOX', 'link_url': '', 'image_url': 'http://files.etsycorp.com/kdaniels/sox.png', 'datafeed_url': None, 'flavor_text': 'Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.', 'is_deleted': False, 'create_date': 1452613520, 'update_date': 1476807538}, {'id': 44818833130, 'badge_name': 'Sweet Pickles', 'badge_alt': 'Sweet pickles, yo.', 'link_url': '', 'image_url': 'http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465403426, 'update_date': 1465403426}, {'id': 43971562858, 'badge_name': '55 Washington', 'badge_alt': 'This badge is for admin who worked in 55 Washington. ', 'link_url': 'https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office', 'image_url': 'https://i.imgur.com/mycU2AQ.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1463593662, 'update_date': 1463686385}, {'id': 35234784233, 'badge_name': 'Impala Friend', 'badge_alt': 'This badge is awarded to people who made friends with the Impala and have installed Dashlane', 'link_url': '', 'image_url': 'https://i.imgur.com/P2p27xS.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1447399868, 'update_date': 1447399868}, {'id': 44342415097, 'badge_name': 'Talent Show 2016', 'badge_alt': 'This is for the talented folks who performed at the 2016 talent show.', 'link_url': '', 'image_url': 'https://i.imgur.com/YZFZ0co.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1460478193, 'update_date': 1460478193}, {'id': 29733526636, 'badge_name': 'I bike to work', 'badge_alt': 'This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ', 'link_url': '', 'image_url': 'https://i.imgur.com/KfLbu6e.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1440531652, 'update_date': 1440612447}, {'id': 43715753559, 'badge_name': 'i survived glibc', 'badge_alt': 'This badge is awarded to anyone who helped out with glibc patching', 'link_url': 'https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html', 'image_url': 'https://i.imgur.com/nF8UIc4.png', 'datafeed_url': None, 'flavor_text': 'and all i got was this lousy badge', 'is_deleted': False, 'create_date': 1459545873, 'update_date': 1459545982}, {'id': 27836203729, 'badge_name': 'Chef', 'badge_alt': 'This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)', 'link_url': 'http://go/chefdocs', 'image_url': 'https://i.imgur.com/5DY6ww8.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437428989, 'update_date': 1458048163}, {'id': 27939260500, 'badge_name': 'Lunch &#39;n&#39; Learners', 'badge_alt': 'This badge is awarded to admin who have given a Lunch and Learn presentation', 'link_url': 'https://jira.etsycorp.com/confluence/display/HR/How+to+Lunch+and+Learn', 'image_url': 'http://content.govdelivery.com/attachments/fancy_images/AKDOA/2013/09/219103/229155/lunch-n-learn-small_original_crop.jpg', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1437404953, 'update_date': 1437404953}, {'id': 28011637847, 'badge_name': 'Badge-Makers Badge', 'badge_alt': 'For those who make badges', 'link_url': '', 'image_url': 'https://i.imgur.com/IsBkGUm.png', 'datafeed_url': None, 'flavor_text': 'Snaaaake! Snaaaake! Ohhhh it&#39;s a snake.', 'is_deleted': False, 'create_date': 1437752815, 'update_date': 1498240151}, {'id': 28466816121, 'badge_name': 'Laptop Healthcheck', 'badge_alt': 'A safe laptop is a good laptop. Thank you for getting your laptop checked by Security and CorpIT.', 'link_url': None, 'image_url': 'https://i.imgur.com/nv1jP9h.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1438697403, 'update_date': 1438697566}, {'id': 27983256371, 'badge_name': 'Datacenter Wizard', 'badge_alt': 'You took the epic journey out to beautiful sunny Secaucus, NJ to visit one of our datacenters!', 'link_url': '', 'image_url': 'https://i.imgur.com/CRhxup2.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437702713, 'update_date': 1506021086}, {'id': 27973621163, 'badge_name': 'F5 Wrangler', 'badge_alt': 'You touch the F5s.  That can (should?) be scary.', 'link_url': '', 'image_url': 'https://i.imgur.com/oa4gBJi.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437688022, 'update_date': 1481922221}, {'id': 27822942841, 'badge_name': 'Vim', 'badge_alt': 'Using vim is it&#39;s own reward, but you still deserve a medal', 'link_url': None, 'image_url': 'https://i.imgur.com/1owm1jW.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1437403904, 'update_date': 1437403904}, {'id': 27723375281, 'badge_name': 'EtsyWeb', 'badge_alt': 'This is for everyone who has pushed code.', 'link_url': '', 'image_url': 'https://i.imgur.com/706zIx4.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437156086, 'update_date': 1564156829}], 'teams': [{'name': 'Security', 'slug': 'security', 'irc_channel': 'security', 'irc_channel_alert_word': 'yeezus, security, brennivin', 'team_location': '117 4th Floor pod 01-015 (NW Corner) - San Jose (Jerry Soung) - Chicago (Adam Enger) - San Diego (Patricio Jara)'}, {'name': 'Security Research and Operations', 'slug': 'security-research-and-operations', 'irc_channel': 'security', 'irc_channel_alert_word': 'netsec-team', 'team_location': '117 4th Floor pod 01-015 (NW Corner)'}, {'name': 'Security Operations Org', 'slug': 'security-operations-org', 'irc_channel': '', 'irc_channel_alert_word': '', 'team_location': 'BK HQ 4th floor & 5th floor, Dublin, Hudson & plenty of remote representation'}]}
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
{'id': 26099105232, 'auth_username': 'ngaffey', 'prefix': '', 'first_name': 'Nuala', 'middle_name': '', 'last_name': 'Gaffey', 'nickname': '', 'suffix': '', 'pronouns': 'she/her', 'gender': '', 'email': 'ngaffey@etsy.com', 'enabled': 1, 'workday_employee_id': '1317', 'department_id': 0, 'employee_type': 'Regular', 'join_date': 1433808000, 'fulltime_date': 0, 'termination_date': 0, 'birthday': '', 'manager_auth_username': 'cclark', 'title': 'Senior Security Engineer II', 'team': 'Infrastructure and Operations', 'office': 'Brooklyn, NY', 'desk_phone': '', 'cell_phone': '6314088045', 'home_phone': '', 'skype': '', 'pager_email': 'ngaffey@etsy.com', 'irc_nick': 'ngaffey', 'slack_nick': 'ngaffey', 'slack_id': 'U27F4A3F0', 'user_id': 67678667, 'login_name': 'nualagaffey', 'shop_name': '', 'twitter': '', 'github': 'nuala33', 'linkedin': '', 'org': 'Cost of Revenue (FSLI)', 'dept': 'Technology - Security', 'group': '', 'phonetic_name': 'Noo-la', 'location': '', 'zendesk_id': 0, 'full_name': 'Nuala Gaffey', 'name': 'Nuala Gaffey', 'short_name': 'Nuala', 'is_manager': True, 'department': 'Infrastructure and Operations', 'avatar': 'https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0', 'badges': [{'id': 389928128051, 'badge_name': 'Local Roots NYC', 'badge_alt': 'This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ', 'link_url': '', 'image_url': 'https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209', 'datafeed_url': None, 'flavor_text': 'Alexa, how do I cook kohlrabi?', 'is_deleted': False, 'create_date': 1535043147, 'update_date': 1541701591}, {'id': 618614020664, 'badge_name': 'Eng Onboarding Lightning Talks', 'badge_alt': 'Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks', 'link_url': '', 'image_url': 'https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1569358386, 'update_date': 1569572097}, {'id': 588523834498, 'badge_name': 'Onboarding Helper', 'badge_alt': 'Thank you for helping during our on-boarding session. We appreciate you.', 'link_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'image_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'datafeed_url': None, 'flavor_text': 'You are a unicorn WOOP WOOP', 'is_deleted': False, 'create_date': 1565717083, 'update_date': 1569953561}, {'id': 39501666387, 'badge_name': 'I visited the Dublin office', 'badge_alt': 'For all the wonderful visitors to the Dublin office', 'link_url': '', 'image_url': 'https://i.imgur.com/QjpsuPK.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1455897522, 'update_date': 1556032479}, {'id': 205062567454, 'badge_name': 'B.A. is for Bad Ass', 'badge_alt': 'No time for B.S. (for Engineers with B.A. Degrees)', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1507926840, 'update_date': 1563393681}, {'id': 49750688293, 'badge_name': 'I see, you see, your yu-bi-key!', 'badge_alt': 'I&#39;ve seen your yubikey ;) They saw your yubikey ;) ', 'link_url': 'https://github.com/pallotron/yubiswitch', 'image_url': 'https://i.imgur.com/HExbKU6.png', 'datafeed_url': None, 'flavor_text': 'mmmm, keys. ', 'is_deleted': False, 'create_date': 1471533753, 'update_date': 1551114177}, {'id': 105074684569, 'badge_name': 'forever VIB', 'badge_alt': 'always buying from sephora just for the samples', 'link_url': '', 'image_url': 'http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357', 'datafeed_url': None, 'flavor_text': 'is it glamglow?', 'is_deleted': False, 'create_date': 1487197073, 'update_date': 1487197073}, {'id': 415079814924, 'badge_name': 'I have accepted Peanut Butter and Pickle into my life', 'badge_alt': 'Everything a grown adult needs for health and vitality', 'link_url': '', 'image_url': 'https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg', 'datafeed_url': None, 'flavor_text': '&quot;Ambrosia&quot; -- Shayne Barr', 'is_deleted': False, 'create_date': 1540850069, 'update_date': 1540850194}, {'id': 210882889226, 'badge_name': 'Atonal Music Lovers', 'badge_alt': 'maybe not, but we tried!', 'link_url': '', 'image_url': 'http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1508965668, 'update_date': 1508965668}, {'id': 331242931409, 'badge_name': 'Coda as Craft', 'badge_alt': 'You&#39;ve sung with Etsy&#39;s a capella group!', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1527108861, 'update_date': 1527108861}, {'id': 319226515931, 'badge_name': 'Certified ScrumMaster ', 'badge_alt': 'You completed the CSM training! ', 'link_url': 'http://scrumguides.org/scrum-guide.html', 'image_url': 'http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1525709146, 'update_date': 1572026189}, {'id': 35378054248, 'badge_name': 'Security Champion', 'badge_alt': 'You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.', 'link_url': '', 'image_url': 'https://i.imgur.com/AHXwccN.png', 'datafeed_url': None, 'flavor_text': '?alertword', 'is_deleted': False, 'create_date': 1447398334, 'update_date': 1570474992}, {'id': 47054459247, 'badge_name': 'Order of Saint Theodore of Feckton', 'badge_alt': 'I have been to Dublin and survived the Engineering Teams.', 'link_url': '', 'image_url': 'https://i.imgur.com/269SaI1.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465813717, 'update_date': 1563277966}, {'id': 35813106870, 'badge_name': 'ELK Wrangler', 'badge_alt': 'For those who have helped wrangle the ELK cluster', 'link_url': '', 'image_url': 'https://i.imgur.com/9l0i7mj.png', 'datafeed_url': None, 'flavor_text': 'A Møøse once bit my sister... No realli!', 'is_deleted': False, 'create_date': 1448475304, 'update_date': 1498240351}, {'id': 64300114379, 'badge_name': 'Golden SOX', 'badge_alt': 'This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX', 'link_url': '', 'image_url': 'https://i.imgur.com/LX2CQWk.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': True, 'create_date': 1478875468, 'update_date': 1570568682}, {'id': 34566765264, 'badge_name': 'I&#39;ve done doubles dev!', 'badge_alt': 'You&#39;ve done doubles! ', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg', 'datafeed_url': None, 'flavor_text': 'DD 4 EVA', 'is_deleted': False, 'create_date': 1445969385, 'update_date': 1558027395}, {'id': 38011401266, 'badge_name': 'SOX', 'badge_alt': 'For service above and beyond the call of duty in the line of SOX', 'link_url': '', 'image_url': 'http://files.etsycorp.com/kdaniels/sox.png', 'datafeed_url': None, 'flavor_text': 'Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.', 'is_deleted': False, 'create_date': 1452613520, 'update_date': 1476807538}, {'id': 44818833130, 'badge_name': 'Sweet Pickles', 'badge_alt': 'Sweet pickles, yo.', 'link_url': '', 'image_url': 'http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465403426, 'update_date': 1465403426}, {'id': 43971562858, 'badge_name': '55 Washington', 'badge_alt': 'This badge is for admin who worked in 55 Washington. ', 'link_url': 'https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office', 'image_url': 'https://i.imgur.com/mycU2AQ.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1463593662, 'update_date': 1463686385}, {'id': 35234784233, 'badge_name': 'Impala Friend', 'badge_alt': 'This badge is awarded to people who made friends with the Impala and have installed Dashlane', 'link_url': '', 'image_url': 'https://i.imgur.com/P2p27xS.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1447399868, 'update_date': 1447399868}, {'id': 44342415097, 'badge_name': 'Talent Show 2016', 'badge_alt': 'This is for the talented folks who performed at the 2016 talent show.', 'link_url': '', 'image_url': 'https://i.imgur.com/YZFZ0co.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1460478193, 'update_date': 1460478193}, {'id': 29733526636, 'badge_name': 'I bike to work', 'badge_alt': 'This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ', 'link_url': '', 'image_url': 'https://i.imgur.com/KfLbu6e.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1440531652, 'update_date': 1440612447}, {'id': 43715753559, 'badge_name': 'i survived glibc', 'badge_alt': 'This badge is awarded to anyone who helped out with glibc patching', 'link_url': 'https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html', 'image_url': 'https://i.imgur.com/nF8UIc4.png', 'datafeed_url': None, 'flavor_text': 'and all i got was this lousy badge', 'is_deleted': False, 'create_date': 1459545873, 'update_date': 1459545982}, {'id': 27836203729, 'badge_name': 'Chef', 'badge_alt': 'This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)', 'link_url': 'http://go/chefdocs', 'image_url': 'https://i.imgur.com/5DY6ww8.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437428989, 'update_date': 1458048163}, {'id': 27939260500, 'badge_name': 'Lunch &#39;n&#39; Learners', 'badge_alt': 'This badge is awarded to admin who have given a Lunch and Learn presentation', 'link_url': praghav@6622 Chef % clear

praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
{'id': 26099105232, 'auth_username': 'ngaffey', 'prefix': '', 'first_name': 'Nuala', 'middle_name': '', 'last_name': 'Gaffey', 'nickname': '', 'suffix': '', 'pronouns': 'she/her', 'gender': '', 'email': 'ngaffey@etsy.com', 'enabled': 1, 'workday_employee_id': '1317', 'department_id': 0, 'employee_type': 'Regular', 'join_date': 1433808000, 'fulltime_date': 0, 'termination_date': 0, 'birthday': '', 'manager_auth_username': 'cclark', 'title': 'Senior Security Engineer II', 'team': 'Infrastructure and Operations', 'office': 'Brooklyn, NY', 'desk_phone': '', 'cell_phone': '6314088045', 'home_phone': '', 'skype': '', 'pager_email': 'ngaffey@etsy.com', 'irc_nick': 'ngaffey', 'slack_nick': 'ngaffey', 'slack_id': 'U27F4A3F0', 'user_id': 67678667, 'login_name': 'nualagaffey', 'shop_name': '', 'twitter': '', 'github': 'nuala33', 'linkedin': '', 'org': 'Cost of Revenue (FSLI)', 'dept': 'Technology - Security', 'group': '', 'phonetic_name': 'Noo-la', 'location': '', 'zendesk_id': 0, 'full_name': 'Nuala Gaffey', 'name': 'Nuala Gaffey', 'short_name': 'Nuala', 'is_manager': True, 'department': 'Infrastructure and Operations', 'avatar': 'https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0', 'badges': [{'id': 389928128051, 'badge_name': 'Local Roots NYC', 'badge_alt': 'This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ', 'link_url': '', 'image_url': 'https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209', 'datafeed_url': None, 'flavor_text': 'Alexa, how do I cook kohlrabi?', 'is_deleted': False, 'create_date': 1535043147, 'update_date': 1541701591}, {'id': 618614020664, 'badge_name': 'Eng Onboarding Lightning Talks', 'badge_alt': 'Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks', 'link_url': '', 'image_url': 'https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1569358386, 'update_date': 1569572097}, {'id': 588523834498, 'badge_name': 'Onboarding Helper', 'badge_alt': 'Thank you for helping during our on-boarding session. We appreciate you.', 'link_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'image_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'datafeed_url': None, 'flavor_text': 'You are a unicorn WOOP WOOP', 'is_deleted': False, 'create_date': 1565717083, 'update_date': 1569953561}, {'id': 39501666387, 'badge_name': 'I visited the Dublin office', 'badge_alt': 'For all the wonderful visitors to the Dublin office', 'link_url': '', 'image_url': 'https://i.imgur.com/QjpsuPK.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1455897522, 'update_date': 1556032479}, {'id': 205062567454, 'badge_name': 'B.A. is for Bad Ass', 'badge_alt': 'No time for B.S. (for Engineers with B.A. Degrees)', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1507926840, 'update_date': 1563393681}, {'id': 49750688293, 'badge_name': 'I see, you see, your yu-bi-key!', 'badge_alt': 'I&#39;ve seen your yubikey ;) They saw your yubikey ;) ', 'link_url': 'https://github.com/pallotron/yubiswitch', 'image_url': 'https://i.imgur.com/HExbKU6.png', 'datafeed_url': None, 'flavor_text': 'mmmm, keys. ', 'is_deleted': False, 'create_date': 1471533753, 'update_date': 1551114177}, {'id': 105074684569, 'badge_name': 'forever VIB', 'badge_alt': 'always buying from sephora just for the samples', 'link_url': '', 'image_url': 'http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357', 'datafeed_url': None, 'flavor_text': 'is it glamglow?', 'is_deleted': False, 'create_date': 1487197073, 'update_date': 1487197073}, {'id': 415079814924, 'badge_name': 'I have accepted Peanut Butter and Pickle into my life', 'badge_alt': 'Everything a grown adult needs for health and vitality', 'link_url': '', 'image_url': 'https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg', 'datafeed_url': None, 'flavor_text': '&quot;Ambrosia&quot; -- Shayne Barr', 'is_deleted': False, 'create_date': 1540850069, 'update_date': 1540850194}, {'id': 210882889226, 'badge_name': 'Atonal Music Lovers', 'badge_alt': 'maybe not, but we tried!', 'link_url': '', 'image_url': 'http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1508965668, 'update_date': 1508965668}, {'id': 331242931409, 'badge_name': 'Coda as Craft', 'badge_alt': 'You&#39;ve sung with Etsy&#39;s a capella group!', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1527108861, 'update_date': 1527108861}, {'id': 319226515931, 'badge_name': 'Certified ScrumMaster ', 'badge_alt': 'You completed the CSM training! ', 'link_url': 'http://scrumguides.org/scrum-guide.html', 'image_url': 'http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1525709146, 'update_date': 1572026189}, {'id': 35378054248, 'badge_name': 'Security Champion', 'badge_alt': 'You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.', 'link_url': '', 'image_url': 'https://i.imgur.com/AHXwccN.png', 'datafeed_url': None, 'flavor_text': '?alertword', 'is_deleted': False, 'create_date': 1447398334, 'update_date': 1570474992}, {'id': 47054459247, 'badge_name': 'Order of Saint Theodore of Feckton', 'badge_alt': 'I have been to Dublin and survived the Engineering Teams.', 'link_url': '', 'image_url': 'https://i.imgur.com/269SaI1.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465813717, 'update_date': 1563277966}, {'id': 35813106870, 'badge_name': 'ELK Wrangler', 'badge_alt': 'For those who have helped wrangle the ELK cluster', 'link_url': '', 'image_url': 'https://i.imgur.com/9l0i7mj.png', 'datafeed_url': None, 'flavor_text': 'A Møøse once bit my sister... No realli!', 'is_deleted': False, 'create_date': 1448475304, 'update_date': 1498240351}, {'id': 64300114379, 'badge_name': 'Golden SOX', 'badge_alt': 'This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX', 'link_url': '', 'image_url': 'https://i.imgur.com/LX2CQWk.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': True, 'create_date': 1478875468, 'update_date': 1570568682}, {'id': 34566765264, 'badge_name': 'I&#39;ve done doubles dev!', 'badge_alt': 'You&#39;ve done doubles! ', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg', 'datafeed_url': None, 'flavor_text': 'DD 4 EVA', 'is_deleted': False, 'create_date': 1445969385, 'update_date': 1558027395}, {'id': 38011401266, 'badge_name': 'SOX', 'badge_alt': 'For service above and beyond the call of duty in the line of SOX', 'link_url': '', 'image_url': 'http://files.etsycorp.com/kdaniels/sox.png', 'datafeed_url': None, 'flavor_text': 'Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.', 'is_deleted': False, 'create_date': 1452613520, 'update_date': 1476807538}, {'id': 44818833130, 'badge_name': 'Sweet Pickles', 'badge_alt': 'Sweet pickles, yo.', 'link_url': '', 'image_url': 'http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465403426, 'update_date': 1465403426}, {'id': 43971562858, 'badge_name': '55 Washington', 'badge_alt': 'This badge is for admin who worked in 55 Washington. ', 'link_url': 'https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office', 'image_url': 'https://i.imgur.com/mycU2AQ.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1463593662, 'update_date': 1463686385}, {'id': 35234784233, 'badge_name': 'Impala Friend', 'badge_alt': 'This badge is awarded to people who made friends with the Impala and have installed Dashlane', 'link_url': '', 'image_url': 'https://i.imgur.com/P2p27xS.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1447399868, 'update_date': 1447399868}, {'id': 44342415097, 'badge_name': 'Talent Show 2016', 'badge_alt': 'This is for the talented folks who performed at the 2016 talent show.', 'link_url': '', 'image_url': 'https://i.imgur.com/YZFZ0co.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1460478193, 'update_date': 1460478193}, {'id': 29733526636, 'badge_name': 'I bike to work', 'badge_alt': 'This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ', 'link_url': '', 'image_url': 'https://i.imgur.com/KfLbu6e.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1440531652, 'update_date': 1440612447}, {'id': 43715753559, 'badge_name': 'i survived glibc', 'badge_alt': 'This badge is awarded to anyone who helped out with glibc patching', 'link_url': 'https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html', 'image_url': 'https://i.imgur.com/nF8UIc4.png', 'datafeed_url': None, 'flavor_text': 'and all i got was this lousy badge', 'is_deleted': False, 'create_date': 1459545873, 'update_date': 1459545982}, {'id': 27836203729, 'badge_name': 'Chef', 'badge_alt': 'This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)', 'link_url': 'http://go/chefdocs', 'image_url': 'https://i.imgur.com/5DY6ww8.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437428989, 'update_date': 1458048163}, {'id': 27939260500, 'badge_name': 'Lunch &#39;n&#39; Learners', 'badge_alt': 'This badge is awarded to admin who have given a Lunch and Learn presentation', 'link_url': praghav@6622 Chef % clear

praghav@6622 Chef % vim URL_Access.py                                                                                
praghav@6622 Chef % rm file.text 
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	hash.text	pattern.py	web_scrapper.py
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
Traceback (most recent call last):
  File "URL_Access.py", line 40, in <module>
    main()
  File "URL_Access.py", line 37, in main
    filtering(git_url)  
  File "URL_Access.py", line 21, in filtering
    wfile.write(data)
NameError: name 'data' is not defined
...skipping...
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
...skipping...
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
...skipping...
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
praghav@6622 Chef % vim URL_Access.py                                                                                
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
Traceback (most recent call last):
  File "URL_Access.py", line 39, in <module>
    main()
  File "URL_Access.py", line 36, in main
{'id': 26099105232, 'auth_username': 'ngaffey', 'prefix': '', 'first_name': 'Nuala', 'middle_name': '', 'last_name': 'Gaffey', 'nickname': '', 'suffix': '', 'pronouns': 'she/her', 'gender': '', 'email': 'ngaffey@etsy.com', 'enabled': 1, 'workday_employee_id': '1317', 'department_id': 0, 'employee_type': 'Regular', 'join_date': 1433808000, 'fulltime_date': 0, 'termination_date': 0, 'birthday': '', 'manager_auth_username': 'cclark', 'title': 'Senior Security Engineer II', 'team': 'Infrastructure and Operations', 'office': 'Brooklyn, NY', 'desk_phone': '', 'cell_phone': '6314088045', 'home_phone': '', 'skype': '', 'pager_email': 'ngaffey@etsy.com', 'irc_nick': 'ngaffey', 'slack_nick': 'ngaffey', 'slack_id': 'U27F4A3F0', 'user_id': 67678667, 'login_name': 'nualagaffey', 'shop_name': '', 'twitter': '', 'github': 'nuala33', 'linkedin': '', 'org': 'Cost of Revenue (FSLI)', 'dept': 'Technology - Security', 'group': '', 'phonetic_name': 'Noo-la', 'location': '', 'zendesk_id': 0, 'full_name': 'Nuala Gaffey', '    filtering(git_url)  
  File "URL_Access.py", line 18, in filtering
    wfile.write(data)   
TypeError: write() argument must be str, not dict
name': 'Nuala Gaffey', 'short_name': 'Nuala', 'is_manager': True, 'department': 'Infrastructure and Operations', 'avatar': 'https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0', 'badges': [{'id': 389928128051, 'badge_name': 'Local Roots NYC', 'badge_alt': 'This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ', 'link_url': '', 'image_url': 'https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209', 'datafeed_url': None, 'flavor_text': 'Alexa, how do I cook kohlrabi?', 'is_deleted': False, 'create_date': 1535043147, 'update_date': 1541701591}, {'id': 618614020664, 'badge_name': 'Eng Onboarding Lightning Talks', 'badge_alt': 'Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks', 'link_url': '', 'image_url': 'https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1569358386, 'update_date': 1569572097}, {'id': 588523834498, 'badge_name': 'Onboarding Helper', 'badge_alt': 'Thank you for helping during our on-boarding session. We appreciate you.', 'link_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'image_url': 'http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png', 'datafeed_url': None, 'flavor_text': 'You are a unicorn WOOP WOOP', 'is_deleted': False, 'create_date': 1565717083, 'update_date': 1569953561}, {'id': 39501666387, 'badge_name': 'I visited the Dublin office', 'badge_alt': 'For all the wonderful visitors to the Dublin office', 'link_url': '', 'image_url': 'https://i.imgur.com/QjpsuPK.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1455897522, 'update_date': 1556032479}, {'id': 205062567454, 'badge_name': 'B.A. is for Bad Ass', 'badge_alt': 'No time for B.S. (for Engineers with B.A. Degrees)', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1507926840, 'update_date': 1563393681}, {'id': 49750688293, 'badge_name': 'I see, you see, your yu-bi-key!', 'badge_alt': 'I&#39;ve seen your yubikey ;) They saw your yubikey ;) ', 'link_url': 'https://github.com/pallotron/yubiswitch', 'image_url': 'https://i.imgur.com/HExbKU6.png', 'datafeed_url': None, 'flavor_text': 'mmmm, keys. ', 'is_deleted': False, 'create_date': 1471533753, 'update_date': 1551114177}, {'id': 105074684569, 'badge_name': 'forever VIB', 'badge_alt': 'always buying from sephora just for the samples', 'link_url': '', 'image_url': 'http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357', 'datafeed_url': None, 'flavor_text': 'is it glamglow?', 'is_deleted': False, 'create_date': 1487197073, 'update_date': 1487197073}, {'id': 415079814924, 'badge_name': 'I have accepted Peanut Butter and Pickle into my life', 'badge_alt': 'Everything a grown adult needs for health and vitality', 'link_url': '', 'image_url': 'https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg', 'datafeed_url': None, 'flavor_text': '&quot;Ambrosia&quot; -- Shayne Barr', 'is_deleted': False, 'create_date': 1540850069, 'update_date': 1540850194}, {'id': 210882889226, 'badge_name': 'Atonal Music Lovers', 'badge_alt': 'maybe not, but we tried!', 'link_url': '', 'image_url': 'http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1508965668, 'update_date': 1508965668}, {'id': 331242931409, 'badge_name': 'Coda as Craft', 'badge_alt': 'You&#39;ve sung with Etsy&#39;s a capella group!', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1527108861, 'update_date': 1527108861}, {'id': 319226515931, 'badge_name': 'Certified ScrumMaster ', 'badge_alt': 'You completed the CSM training! ', 'link_url': 'http://scrumguides.org/scrum-guide.html', 'image_url': 'http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1525709146, 'update_date': 1572026189}, {'id': 35378054248, 'badge_name': 'Security Champion', 'badge_alt': 'You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.', 'link_url': '', 'image_url': 'https://i.imgur.com/AHXwccN.png', 'datafeed_url': None, 'flavor_text': '?alertword', 'is_deleted': False, 'create_date': 1447398334, 'update_date': 1570474992}, {'id': 47054459247, 'badge_name': 'Order of Saint Theodore of Feckton', 'badge_alt': 'I have been to Dublin and survived the Engineering Teams.', 'link_url': '', 'image_url': 'https://i.imgur.com/269SaI1.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465813717, 'update_date': 1563277966}, {'id': 35813106870, 'badge_name': 'ELK Wrangler', 'badge_alt': 'For those who have helped wrangle the ELK cluster', 'link_url': '', 'image_url': 'https://i.imgur.com/9l0i7mj.png', 'datafeed_url': None, 'flavor_text': 'A Møøse once bit my sister... No realli!', 'is_deleted': False, 'create_date': 1448475304, 'update_date': 1498240351}, {'id': 64300114379, 'badge_name': 'Golden SOX', 'badge_alt': 'This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX', 'link_url': '', 'image_url': 'https://i.imgur.com/LX2CQWk.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': True, 'create_date': 1478875468, 'update_date': 1570568682}, {'id': 34566765264, 'badge_name': 'I&#39;ve done doubles dev!', 'badge_alt': 'You&#39;ve done doubles! ', 'link_url': '', 'image_url': 'http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg', 'datafeed_url': None, 'flavor_text': 'DD 4 EVA', 'is_deleted': False, 'create_date': 1445969385, 'update_date': 1558027395}, {'id': 38011401266, 'badge_name': 'SOX', 'badge_alt': 'For service above and beyond the call of duty in the line of SOX', 'link_url': '', 'image_url': 'http://files.etsycorp.com/kdaniels/sox.png', 'datafeed_url': None, 'flavor_text': 'Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.', 'is_deleted': False, 'create_date': 1452613520, 'update_date': 1476807538}, {'id': 44818833130, 'badge_name': 'Sweet Pickles', 'badge_alt': 'Sweet pickles, yo.', 'link_url': '', 'image_url': 'http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1465403426, 'update_date': 1465403426}, {'id': 43971562858, 'badge_name': '55 Washington', 'badge_alt': 'This badge is for admin who worked in 55 Washington. ', 'link_url': 'https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office', 'image_url': 'https://i.imgur.com/mycU2AQ.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1463593662, 'update_date': 1463686385}, {'id': 35234784233, 'badge_name': 'Impala Friend', 'badge_alt': 'This badge is awarded to people who made friends with the Impala and have installed Dashlane', 'link_url': '', 'image_url': 'https://i.imgur.com/P2p27xS.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1447399868, 'update_date': 1447399868}, {'id': 44342415097, 'badge_name': 'Talent Show 2016', 'badge_alt': 'This is for the talented folks who performed at the 2016 talent show.', 'link_url': '', 'image_url': 'https://i.imgur.com/YZFZ0co.png', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1460478193, 'update_date': 1460478193}, {'id': 29733526636, 'badge_name': 'I bike to work', 'badge_alt': 'This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ', 'link_url': '', 'image_url': 'https://i.imgur.com/KfLbu6e.png', 'datafeed_url': None, 'flavor_text': None, 'is_deleted': False, 'create_date': 1440531652, 'update_date': 1440612447}, {'id': 43715753559, 'badge_name': 'i survived glibc', 'badge_alt': 'This badge is awarded to anyone who helped out with glibc patching', 'link_url': 'https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html', 'image_url': 'https://i.imgur.com/nF8UIc4.png', 'datafeed_url': None, 'flavor_text': 'and all i got was this lousy badge', 'is_deleted': False, 'create_date': 1459545873, 'update_date': 1459545982}, {'id': 27836203729, 'badge_name': 'Chef', 'badge_alt': 'This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)', 'link_url': 'http://go/chefdocs', 'image_url': 'https://i.imgur.com/5DY6ww8.jpg', 'datafeed_url': None, 'flavor_text': '', 'is_deleted': False, 'create_date': 1437428989, 'update_date': 1458048163}, {'id': 27939260500, 'badge_name': 'Lunch &#39;n&#39; Learners', 'badge_alt': 'This badge is awarded to admin who have given a Lunch and Learn presentation', 'link_upraghav@6622 Chef % 
praghav@6622 Chef % vim URL_Access.py                                                                                
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
Traceback (most recent call last):
  File "URL_Access.py", line 38, in <module>
    main()
  File "URL_Access.py", line 35, in main
    filtering(git_url)  
  File "URL_Access.py", line 17, in filtering
    wfile.write(data)   
TypeError: write() argument must be str, not dict
praghav@6622 Chef % vim URL_Access.py                                                                                
praghav@6622 Chef % python3.8 URL_Access.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
Traceback (most recent call last):
  File "URL_Access.py", line 39, in <module>
    main()
  File "URL_Access.py", line 36, in main
    filtering(git_url)  
  File "URL_Access.py", line 17, in filtering
    wfile.write(data)
TypeError: write() argument must be str, not dict
 ESCESC...skipping...
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
 :w...skipping...
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
praghav@6622 Chef % clear

praghav@6622 Chef % vim request.py
praghav@6622 Chef % python3.8 request.py 
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 39501666387,
            "image_url": "https://i.imgur.com/QjpsuPK.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1556032479
        },
        {
            "badge_alt": "No time for B.S. (for Engineers with B.A. Degrees)",
            "badge_name": "B.A. is for Bad Ass",
            "create_date": 1507926840,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 205062567454,
            "image_url": "http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563393681
        },
        {
            "badge_alt": "I&#39;ve seen your yubikey ;) They saw your yubikey ;) ",
            "badge_name": "I see, you see, your yu-bi-key!",
            "create_date": 1471533753,
            "datafeed_url": null,
            "flavor_text": "mmmm, keys. ",
            "id": 49750688293,
            "image_url": "https://i.imgur.com/HExbKU6.png",
            "is_deleted": false,
            "link_url": "https://github.com/pallotron/yubiswitch",
            "update_date": 1551114177
        },
        {
            "badge_alt": "always buying from sephora just for the samples",
            "badge_name": "forever VIB",
            "create_date": 1487197073,
            "datafeed_url": null,
            "flavor_text": "is it glamglow?",
            "id": 105074684569,
            "image_url": "http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1487197073
        },
        {
            "badge_alt": "Everything a grown adult needs for health and vitality",
            "badge_name": "I have accepted Peanut Butter and Pickle into my life",
            "create_date": 1540850069,
            "datafeed_url": null,
            "flavor_text": "&quot;Ambrosia&quot; -- Shayne Barr",
            "id": 415079814924,
            "image_url": "https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1540850194
        },
        {
            "badge_alt": "maybe not, but we tried!",
            "badge_name": "Atonal Music Lovers",
            "create_date": 1508965668,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 210882889226,
            "image_url": "http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1508965668
        },
        {
            "badge_alt": "You&#39;ve sung with Etsy&#39;s a capella group!",
            "badge_name": "Coda as Craft",
            "create_date": 1527108861,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 331242931409,
            "image_url": "http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1527108861
        },
        {
            "badge_alt": "You completed the CSM training! ",
            "badge_name": "Certified ScrumMaster ",
            "create_date": 1525709146,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 319226515931,
            "image_url": "http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4",
            "is_deleted": false,
            "link_url": "http://scrumguides.org/scrum-guide.html",
            "update_date": 1572026189
        },
        {
            "badge_alt": "You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.",
            "badge_name": "Security Champion",
            "create_date": 1447398334,
            "datafeed_url": null,
            "flavor_text": "?alertword",
            "id": 35378054248,
            "image_url": "https://i.imgur.com/AHXwccN.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1570474992
        },
        {
            "badge_alt": "I have been to Dublin and survived the Engineering Teams.",
            "badge_name": "Order of Saint Theodore of Feckton",
            "create_date": 1465813717,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 47054459247,
            "image_url": "https://i.imgur.com/269SaI1.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563277966
        },
        {
            "badge_alt": "For those who have helped wrangle the ELK cluster",
            "badge_name": "ELK Wrangler",
            "create_date": 1448475304,
            "datafeed_url": null,
            "flavor_text": "A M\u00f8\u00f8se once bit my sister... No realli!",
            "id": 35813106870,
            "image_url": "https://i.imgur.com/9l0i7mj.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240351
        },
        {
            "badge_alt": "This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX",
            "badge_name": "Golden SOX",
            "create_date": 1478875468,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 64300114379,
            "image_url": "https://i.imgur.com/LX2CQWk.jpg",
            "is_deleted": true,
            "link_url": "",
            "update_date": 1570568682
        },
        {
            "badge_alt": "You&#39;ve done doubles! ",
            "badge_name": "I&#39;ve done doubles dev!",
            "create_date": 1445969385,
            "datafeed_url": null,
            "flavor_text": "DD 4 EVA",
            "id": 34566765264,
            "image_url": "http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1558027395
        },
        {
            "badge_alt": "For service above and beyond the call of duty in the line of SOX",
            "badge_name": "SOX",
            "create_date": 1452613520,
            "datafeed_url": null,
            "flavor_text": "Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.",
            "id": 38011401266,
            "image_url": "http://files.etsycorp.com/kdaniels/sox.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1476807538
        },
        {
            "badge_alt": "Sweet pickles, yo.",
            "badge_name": "Sweet Pickles",
            "create_date": 1465403426,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44818833130,
            "image_url": "http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1465403426
        },
        {
            "badge_alt": "This badge is for admin who worked in 55 Washington. ",
            "badge_name": "55 Washington",
            "create_date": 1463593662,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 43971562858,
            "image_url": "https://i.imgur.com/mycU2AQ.png",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office",
            "update_date": 1463686385
        },
        {
            "badge_alt": "This badge is awarded to people who made friends with the Impala and have installed Dashlane",
            "badge_name": "Impala Friend",
            "create_date": 1447399868,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 35234784233,
            "image_url": "https://i.imgur.com/P2p27xS.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1447399868
        },
        {
            "badge_alt": "This is for the talented folks who performed at the 2016 talent show.",
            "badge_name": "Talent Show 2016",
            "create_date": 1460478193,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44342415097,
            "image_url": "https://i.imgur.com/YZFZ0co.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1460478193
        },
        {
            "badge_alt": "This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ",
            "badge_name": "I bike to work",
            "create_date": 1440531652,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 29733526636,
            "image_url": "https://i.imgur.com/KfLbu6e.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1440612447
        },
        {
            "badge_alt": "This badge is awarded to anyone who helped out with glibc patching",
            "badge_name": "i survived glibc",
            "create_date": 1459545873,
            "datafeed_url": null,
            "flavor_text": "and all i got was this lousy badge",
            "id": 43715753559,
            "image_url": "https://i.imgur.com/nF8UIc4.png",
            "is_deleted": false,
            "link_url": "https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html",
            "update_date": 1459545982
        },
        {
            "badge_alt": "This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)",
            "badge_name": "Chef",
            "create_date": 1437428989,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27836203729,
            "image_url": "https://i.imgur.com/5DY6ww8.jpg",
            "is_deleted": false,
            "link_url": "http://go/chefdocs",
            "update_date": 1458048163
        },
        {
            "badge_alt": "This badge is awarded to admin who have given a Lunch and Learn presentation",
            "badge_name": "Lunch &#39;n&#39; Learners",
            "create_date": 1437404953,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27939260500,
            "image_url": "http://content.govdelivery.com/attachments/fancy_images/AKDOA/2013/09/219103/229155/lunch-n-learn-small_original_crop.jpg",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/HR/How+to+Lunch+and+Learn",
            "update_date": 1437404953
        },
        {
            "badge_alt": "For those who make badges",
            "badge_name": "Badge-Makers Badge",
            "create_date": 1437752815,
            "datafeed_url": null,
            "flavor_text": "Snaaaake! Snaaaake! Ohhhh it&#39;s a snake.",
            "id": 28011637847,
            "image_url": "https://i.imgur.com/IsBkGUm.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240151
        },
        {
            "badge_alt": "A safe laptop is a good laptop. Thank you for getting your laptop checked by Security and CorpIT.",
            "badge_name": "Laptop Healthcheck",
            "create_date": 1438697403,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 28466816121,
            "image_url": "https://i.imgur.com/nv1jP9h.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1438697566
        },
        {
            "badge_alt": "You took the epic journey out to beautiful sunny Secaucus, NJ to visit one of our datacenters!",
            "badge_name": "Datacenter Wizard",
            "create_date": 1437702713,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27983256371,
            "image_url": "https://i.imgur.com/CRhxup2.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1506021086
        },
        {
            "badge_alt": "You touch the F5s.  That can (should?) be scary.",
            "badge_name": "F5 Wrangler",
            "create_date": 1437688022,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27973621163,
            "image_url": "https://i.imgur.com/oa4gBJi.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1481922221
        },
        {
            "badge_alt": "Using vim is it&#39;s own reward, but you still deserve a medal",
            "badge_name": "Vim",
            "create_date": 1437403904,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27822942841,
            "image_url": "https://i.imgur.com/1owm1jW.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1437403904
        },
        {
            "badge_alt": "This is for everyone who has pushed code.",
            "badge_name": "EtsyWeb",
            "create_date": 1437156086,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27723375281,
            "image_url": "https://i.imgur.com/706zIx4.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1564156829
        }
    ],
    "birthday": "",
    "cell_phone": "6314088045",
    "department": "Infrastructure and Operations",
    "department_id": 0,
    "dept": "Technology - Security",
    "desk_phone": "",
    "email": "ngaffey@etsy.com",
    "employee_type": "Regular",
    "enabled": 1,
    "first_name": "Nuala",
    "full_name": "Nuala Gaffey",
    "fulltime_date": 0,
    "gender": "",
    "github": "nuala33",
    "group": "",
    "home_phone": "",
    "id": 26099105232,
    "irc_nick": "ngaffey",
    "is_manager": true,
    "join_date": 1433808000,
    "last_name": "Gaffey",
    "linkedin": "",
    "location": "",
    "login_name": "nualagaffey",
    "manager_auth_username": "cclark",
    "middle_name": "",
    "name": "Nuala Gaffey",
    "nickname": "",
    "office": "Brooklyn, NY",
    "org": "Cost of Revenue (FSLI)",
    "pager_email": "ngaffey@etsy.com",
    "phonetic_name": "Noo-la",
    "prefix": "",
    "pronouns": "she/her",
    "shop_name": "",
    "short_name": "Nuala",
    "skype": "",
    "slack_id": "U27F4A3F0",
    "slack_nick": "ngaffey",
    "suffix": "",
    "team": "Infrastructure and Operations",
    "teams": [
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "yeezus, security, brennivin",
            "name": "Security",
            "slug": "security",
            "team_location": "117 4th Floor pod 01-015 (NW Corner) - San Jose (Jerry Soung) - Chicago (Adam Enger) - San Diego (Patricio Jara)"
        },
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "netsec-team",
            "name": "Security Research and Operations",
            "slug": "security-research-and-operations",
            "team_location": "117 4th Floor pod 01-015 (NW Corner)"
        },
        {
            "irc_channel": "",
            "irc_channel_alert_word": "",
            "name": "Security Operations Org",
            "slug": "security-operations-org",
            "team_location": "BK HQ 4th floor & 5th floor, Dublin, Hudson & plenty of remote representation"
        }
    ],
    "termination_date": 0,
    "title": "Senior Security Engineer II",
    "twitter": "",
    "user_id": 67678667,
    "workday_employee_id": "1317",
    "zendesk_id": 0
}
praghav@6622 Chef % python3.8 request.py | more
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 39501666387,
            "image_url": "https://i.imgur.com/QjpsuPK.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1556032479
        },
praghav@6622 Chef % clear

praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	request.py	web_scrapper.py
praghav@6622 Chef % vim request.py 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"  
Traceback (most recent call last):
  File "request.py", line 28, in <module>
    main()
  File "request.py", line 17, in main
    parser = OptionParser()
NameError: name 'OptionParser' is not defined
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 39501666387,
            "image_url": "https://i.imgur.com/QjpsuPK.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1556032479
        },
        {
            "badge_alt": "No time for B.S. (for Engineers with B.A. Degrees)",
            "badge_name": "B.A. is for Bad Ass",
            "create_date": 1507926840,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 205062567454,
            "image_url": "http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563393681
        },
        {
            "badge_alt": "I&#39;ve seen your yubikey ;) They saw your yubikey ;) ",
            "badge_name": "I see, you see, your yu-bi-key!",
            "create_date": 1471533753,
            "datafeed_url": null,
            "flavor_text": "mmmm, keys. ",
            "id": 49750688293,
            "image_url": "https://i.imgur.com/HExbKU6.png",
            "is_deleted": false,
            "link_url": "https://github.com/pallotron/yubiswitch",
            "update_date": 1551114177
        },
        {
            "badge_alt": "always buying from sephora just for the samples",
            "badge_name": "forever VIB",
            "create_date": 1487197073,
            "datafeed_url": null,
            "flavor_text": "is it glamglow?",
            "id": 105074684569,
            "image_url": "http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1487197073
        },
        {
            "badge_alt": "Everything a grown adult needs for health and vitality",
            "badge_name": "I have accepted Peanut Butter and Pickle into my life",
            "create_date": 1540850069,
            "datafeed_url": null,
            "flavor_text": "&quot;Ambrosia&quot; -- Shayne Barr",
            "id": 415079814924,
            "image_url": "https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1540850194
        },
        {
            "badge_alt": "maybe not, but we tried!",
            "badge_name": "Atonal Music Lovers",
            "create_date": 1508965668,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 210882889226,
            "image_url": "http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1508965668
        },
        {
            "badge_alt": "You&#39;ve sung with Etsy&#39;s a capella group!",
            "badge_name": "Coda as Craft",
            "create_date": 1527108861,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 331242931409,
            "image_url": "http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1527108861
        },
        {
            "badge_alt": "You completed the CSM training! ",
            "badge_name": "Certified ScrumMaster ",
            "create_date": 1525709146,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 319226515931,
            "image_url": "http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4",
            "is_deleted": false,
            "link_url": "http://scrumguides.org/scrum-guide.html",
            "update_date": 1572026189
        },
        {
            "badge_alt": "You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.",
            "badge_name": "Security Champion",
            "create_date": 1447398334,
            "datafeed_url": null,
            "flavor_text": "?alertword",
            "id": 35378054248,
            "image_url": "https://i.imgur.com/AHXwccN.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1570474992
        },
        {
            "badge_alt": "I have been to Dublin and survived the Engineering Teams.",
            "badge_name": "Order of Saint Theodore of Feckton",
            "create_date": 1465813717,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 47054459247,
            "image_url": "https://i.imgur.com/269SaI1.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563277966
        },
        {
            "badge_alt": "For those who have helped wrangle the ELK cluster",
            "badge_name": "ELK Wrangler",
            "create_date": 1448475304,
            "datafeed_url": null,
            "flavor_text": "A M\u00f8\u00f8se once bit my sister... No realli!",
            "id": 35813106870,
            "image_url": "https://i.imgur.com/9l0i7mj.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240351
        },
        {
            "badge_alt": "This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX",
            "badge_name": "Golden SOX",
            "create_date": 1478875468,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 64300114379,
            "image_url": "https://i.imgur.com/LX2CQWk.jpg",
            "is_deleted": true,
            "link_url": "",
            "update_date": 1570568682
        },
        {
            "badge_alt": "You&#39;ve done doubles! ",
            "badge_name": "I&#39;ve done doubles dev!",
            "create_date": 1445969385,
            "datafeed_url": null,
            "flavor_text": "DD 4 EVA",
            "id": 34566765264,
            "image_url": "http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1558027395
        },
        {
            "badge_alt": "For service above and beyond the call of duty in the line of SOX",
            "badge_name": "SOX",
            "create_date": 1452613520,
            "datafeed_url": null,
            "flavor_text": "Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.",
            "id": 38011401266,
            "image_url": "http://files.etsycorp.com/kdaniels/sox.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1476807538
        },
        {
            "badge_alt": "Sweet pickles, yo.",
            "badge_name": "Sweet Pickles",
            "create_date": 1465403426,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44818833130,
            "image_url": "http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1465403426
        },
        {
            "badge_alt": "This badge is for admin who worked in 55 Washington. ",
            "badge_name": "55 Washington",
            "create_date": 1463593662,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 43971562858,
            "image_url": "https://i.imgur.com/mycU2AQ.png",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office",
            "update_date": 1463686385
        },
        {
            "badge_alt": "This badge is awarded to people who made friends with the Impala and have installed Dashlane",
            "badge_name": "Impala Friend",
            "create_date": 1447399868,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 35234784233,
            "image_url": "https://i.imgur.com/P2p27xS.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1447399868
        },
        {
            "badge_alt": "This is for the talented folks who performed at the 2016 talent show.",
            "badge_name": "Talent Show 2016",
            "create_date": 1460478193,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44342415097,
            "image_url": "https://i.imgur.com/YZFZ0co.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1460478193
        },
        {
            "badge_alt": "This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ",
            "badge_name": "I bike to work",
            "create_date": 1440531652,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 29733526636,
            "image_url": "https://i.imgur.com/KfLbu6e.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1440612447
        },
        {
            "badge_alt": "This badge is awarded to anyone who helped out with glibc patching",
            "badge_name": "i survived glibc",
            "create_date": 1459545873,
            "datafeed_url": null,
            "flavor_text": "and all i got was this lousy badge",
            "id": 43715753559,
            "image_url": "https://i.imgur.com/nF8UIc4.png",
            "is_deleted": false,
            "link_url": "https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html",
            "update_date": 1459545982
        },
        {
            "badge_alt": "This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)",
            "badge_name": "Chef",
            "create_date": 1437428989,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27836203729,
            "image_url": "https://i.imgur.com/5DY6ww8.jpg",
            "is_deleted": false,
            "link_url": "http://go/chefdocs",
            "update_date": 1458048163
        },
        {
            "badge_alt": "This badge is awarded to admin who have given a Lunch and Learn presentation",
            "badge_name": "Lunch &#39;n&#39; Learners",
            "create_date": 1437404953,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27939260500,
            "image_url": "http://content.govdelivery.com/attachments/fancy_images/AKDOA/2013/09/219103/229155/lunch-n-learn-small_original_crop.jpg",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/HR/How+to+Lunch+and+Learn",
            "update_date": 1437404953
        },
        {
            "badge_alt": "For those who make badges",
            "badge_name": "Badge-Makers Badge",
            "create_date": 1437752815,
            "datafeed_url": null,
            "flavor_text": "Snaaaake! Snaaaake! Ohhhh it&#39;s a snake.",
            "id": 28011637847,
            "image_url": "https://i.imgur.com/IsBkGUm.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240151
        },
        {
            "badge_alt": "A safe laptop is a good laptop. Thank you for getting your laptop checked by Security and CorpIT.",
            "badge_name": "Laptop Healthcheck",
            "create_date": 1438697403,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 28466816121,
            "image_url": "https://i.imgur.com/nv1jP9h.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1438697566
        },
        {
            "badge_alt": "You took the epic journey out to beautiful sunny Secaucus, NJ to visit one of our datacenters!",
            "badge_name": "Datacenter Wizard",
            "create_date": 1437702713,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27983256371,
            "image_url": "https://i.imgur.com/CRhxup2.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1506021086
        },
        {
            "badge_alt": "You touch the F5s.  That can (should?) be scary.",
            "badge_name": "F5 Wrangler",
            "create_date": 1437688022,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27973621163,
            "image_url": "https://i.imgur.com/oa4gBJi.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1481922221
        },
        {
            "badge_alt": "Using vim is it&#39;s own reward, but you still deserve a medal",
            "badge_name": "Vim",
            "create_date": 1437403904,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27822942841,
            "image_url": "https://i.imgur.com/1owm1jW.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1437403904
        },
        {
            "badge_alt": "This is for everyone who has pushed code.",
            "badge_name": "EtsyWeb",
            "create_date": 1437156086,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27723375281,
            "image_url": "https://i.imgur.com/706zIx4.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1564156829
        }
    ],
    "birthday": "",
    "cell_phone": "6314088045",
    "department": "Infrastructure and Operations",
    "department_id": 0,
    "dept": "Technology - Security",
    "desk_phone": "",
    "email": "ngaffey@etsy.com",
    "employee_type": "Regular",
    "enabled": 1,
    "first_name": "Nuala",
    "full_name": "Nuala Gaffey",
    "fulltime_date": 0,
    "gender": "",
    "github": "nuala33",
    "group": "",
    "home_phone": "",
    "id": 26099105232,
    "irc_nick": "ngaffey",
    "is_manager": true,
    "join_date": 1433808000,
    "last_name": "Gaffey",
    "linkedin": "",
    "location": "",
    "login_name": "nualagaffey",
    "manager_auth_username": "cclark",
    "middle_name": "",
    "name": "Nuala Gaffey",
    "nickname": "",
    "office": "Brooklyn, NY",
    "org": "Cost of Revenue (FSLI)",
    "pager_email": "ngaffey@etsy.com",
    "phonetic_name": "Noo-la",
    "prefix": "",
    "pronouns": "she/her",
    "shop_name": "",
    "short_name": "Nuala",
    "skype": "",
    "slack_id": "U27F4A3F0",
    "slack_nick": "ngaffey",
    "suffix": "",
    "team": "Infrastructure and Operations",
    "teams": [
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "yeezus, security, brennivin",
            "name": "Security",
            "slug": "security",
            "team_location": "117 4th Floor pod 01-015 (NW Corner) - San Jose (Jerry Soung) - Chicago (Adam Enger) - San Diego (Patricio Jara)"
        },
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "netsec-team",
            "name": "Security Research and Operations",
            "slug": "security-research-and-operations",
            "team_location": "117 4th Floor pod 01-015 (NW Corner)"
        },
        {
            "irc_channel": "",
            "irc_channel_alert_word": "",
            "name": "Security Operations Org",
            "slug": "security-operations-org",
            "team_location": "BK HQ 4th floor & 5th floor, Dublin, Hudson & plenty of remote representation"
        }
    ],
    "termination_date": 0,
    "title": "Senior Security Engineer II",
    "twitter": "",
    "user_id": 67678667,
    "workday_employee_id": "1317",
    "zendesk_id": 0
}
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 39501666387,
            "image_url": "https://i.imgur.com/QjpsuPK.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1556032479
        },
praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	request.py	web_scrapper.py
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | mor 
praghav@6622 Chef % clear

praghav@6622 Chef % vim request.py 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" | more
"Infrastructure and Operations"
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"       
"Infrastructure and Operations"
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"       
praghav@6622 Chef % clear














































praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	request.py	web_scrapper.py
praghav@6622 Chef % vim request.py 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=praghav" 
""
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
"Infrastructure and Operations"
praghav@6622 Chef % clear













































praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=amellos" 
"Security"
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
"Infrastructure and Operations"
praghav@6622 Chef % clear
















































praghav@6622 Chef % ls
Chef_hashes.csv	URL_Access.py	file.text	hash.text	pattern.py	request.py	web_scrapper.py
praghav@6622 Chef % vim 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
praghav@6622 Chef % vim request.py 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 12
    print "------------------------------------------------------------"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("------------------------------------------------------------")?
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 28
    git_url = "" 
                ^
TabError: inconsistent use of tabs and spaces in indentation
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 29
    git_url = "" 
                ^
TabError: inconsistent use of tabs and spaces in indentation
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 29
    git_url = "" 
                ^
TabError: inconsistent use of tabs and spaces in indentation
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 41
    operator()
             ^
TabError: inconsistent use of tabs and spaces in indentation
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
"Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
"Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 39501666387,
            "image_url": "https://i.imgur.com/QjpsuPK.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1556032479
        },
        {
            "badge_alt": "No time for B.S. (for Engineers with B.A. Degrees)",
            "badge_name": "B.A. is for Bad Ass",
            "create_date": 1507926840,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 205062567454,
            "image_url": "http://imgshare.etsycorp.com/badges//cu-jobr8yr0g0ccc",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563393681
        },
        {
            "badge_alt": "I&#39;ve seen your yubikey ;) They saw your yubikey ;) ",
            "badge_name": "I see, you see, your yu-bi-key!",
            "create_date": 1471533753,
            "datafeed_url": null,
            "flavor_text": "mmmm, keys. ",
            "id": 49750688293,
            "image_url": "https://i.imgur.com/HExbKU6.png",
            "is_deleted": false,
            "link_url": "https://github.com/pallotron/yubiswitch",
            "update_date": 1551114177
        },
        {
            "badge_alt": "always buying from sephora just for the samples",
            "badge_name": "forever VIB",
            "create_date": 1487197073,
            "datafeed_url": null,
            "flavor_text": "is it glamglow?",
            "id": 105074684569,
            "image_url": "http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/22/Sephora.jpg/revision/latest/scale-to-width-down/200?cb=20080617220357",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1487197073
        },
        {
            "badge_alt": "Everything a grown adult needs for health and vitality",
            "badge_name": "I have accepted Peanut Butter and Pickle into my life",
            "create_date": 1540850069,
            "datafeed_url": null,
            "flavor_text": "&quot;Ambrosia&quot; -- Shayne Barr",
            "id": 415079814924,
            "image_url": "https://imgshare.etsycorp.com/adaud/Badges__Create_new_badge_2018-10-29_17-55-07.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1540850194
        },
        {
            "badge_alt": "maybe not, but we tried!",
            "badge_name": "Atonal Music Lovers",
            "create_date": 1508965668,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 210882889226,
            "image_url": "http://gillespiemusic.com/wp-content/uploads/2013/11/origin_742439983.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1508965668
        },
        {
            "badge_alt": "You&#39;ve sung with Etsy&#39;s a capella group!",
            "badge_name": "Coda as Craft",
            "create_date": 1527108861,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 331242931409,
            "image_url": "http://imgshare.etsycorp.com/badges//d4-jq02c1sm8g0ko",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1527108861
        },
        {
            "badge_alt": "You completed the CSM training! ",
            "badge_name": "Certified ScrumMaster ",
            "create_date": 1525709146,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 319226515931,
            "image_url": "http://imgshare.etsycorp.com/badges//2k-odok2lvfuokc4",
            "is_deleted": false,
            "link_url": "http://scrumguides.org/scrum-guide.html",
            "update_date": 1572026189
        },
        {
            "badge_alt": "You&#39;ve worked with Security, you&#39;ve sought out Security on your projects, you&#39;re down with the Security Clown.",
            "badge_name": "Security Champion",
            "create_date": 1447398334,
            "datafeed_url": null,
            "flavor_text": "?alertword",
            "id": 35378054248,
            "image_url": "https://i.imgur.com/AHXwccN.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1570474992
        },
        {
            "badge_alt": "I have been to Dublin and survived the Engineering Teams.",
            "badge_name": "Order of Saint Theodore of Feckton",
            "create_date": 1465813717,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 47054459247,
            "image_url": "https://i.imgur.com/269SaI1.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1563277966
        },
        {
            "badge_alt": "For those who have helped wrangle the ELK cluster",
            "badge_name": "ELK Wrangler",
            "create_date": 1448475304,
            "datafeed_url": null,
            "flavor_text": "A M\u00f8\u00f8se once bit my sister... No realli!",
            "id": 35813106870,
            "image_url": "https://i.imgur.com/9l0i7mj.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240351
        },
        {
            "badge_alt": "This badge is prestigiously awarded to SOX MVPs to recognize their commitment to SOX",
            "badge_name": "Golden SOX",
            "create_date": 1478875468,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 64300114379,
            "image_url": "https://i.imgur.com/LX2CQWk.jpg",
            "is_deleted": true,
            "link_url": "",
            "update_date": 1570568682
        },
        {
            "badge_alt": "You&#39;ve done doubles! ",
            "badge_name": "I&#39;ve done doubles dev!",
            "create_date": 1445969385,
            "datafeed_url": null,
            "flavor_text": "DD 4 EVA",
            "id": 34566765264,
            "image_url": "http://imgshare.etsycorp.com/jrose/doubles-mirtle-ig.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1558027395
        },
        {
            "badge_alt": "For service above and beyond the call of duty in the line of SOX",
            "badge_name": "SOX",
            "create_date": 1452613520,
            "datafeed_url": null,
            "flavor_text": "Three tickets for the Enron-kings under the sky / Seven for the Worldcom-lords in their halls of stone / Nine for Mortal Humans doomed to die / One for the SEC on its dark throne / In the Land of Sarbanes where the Oxleys lie. / One Ticket to rule them all, One Ticket to find them / One Ticket to bring them all and in compliance bind them.",
            "id": 38011401266,
            "image_url": "http://files.etsycorp.com/kdaniels/sox.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1476807538
        },
        {
            "badge_alt": "Sweet pickles, yo.",
            "badge_name": "Sweet Pickles",
            "create_date": 1465403426,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44818833130,
            "image_url": "http://static.tumblr.com/lda8fvp/yDhm8eb9o/sp_logo_tumblr.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1465403426
        },
        {
            "badge_alt": "This badge is for admin who worked in 55 Washington. ",
            "badge_name": "55 Washington",
            "create_date": 1463593662,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 43971562858,
            "image_url": "https://i.imgur.com/mycU2AQ.png",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/WEaD/Brooklyn+Office",
            "update_date": 1463686385
        },
        {
            "badge_alt": "This badge is awarded to people who made friends with the Impala and have installed Dashlane",
            "badge_name": "Impala Friend",
            "create_date": 1447399868,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 35234784233,
            "image_url": "https://i.imgur.com/P2p27xS.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1447399868
        },
        {
            "badge_alt": "This is for the talented folks who performed at the 2016 talent show.",
            "badge_name": "Talent Show 2016",
            "create_date": 1460478193,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 44342415097,
            "image_url": "https://i.imgur.com/YZFZ0co.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1460478193
        },
        {
            "badge_alt": "This badge is for anyone who chooses two wheels over public transportation or *gasp* a car when commuting to work. Bonus points if you&#39;ve made this decision during the bike to work challenge! ",
            "badge_name": "I bike to work",
            "create_date": 1440531652,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 29733526636,
            "image_url": "https://i.imgur.com/KfLbu6e.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1440612447
        },
        {
            "badge_alt": "This badge is awarded to anyone who helped out with glibc patching",
            "badge_name": "i survived glibc",
            "create_date": 1459545873,
            "datafeed_url": null,
            "flavor_text": "and all i got was this lousy badge",
            "id": 43715753559,
            "image_url": "https://i.imgur.com/nF8UIc4.png",
            "is_deleted": false,
            "link_url": "https://security.googleblog.com/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html",
            "update_date": 1459545982
        },
        {
            "badge_alt": "This badge is for folks that have pushed chef code!  btw, there isn&#39;t a great distribution mech for badges yet, so ping me if you feel like you aughtta have one, (jimbo on irc)",
            "badge_name": "Chef",
            "create_date": 1437428989,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27836203729,
            "image_url": "https://i.imgur.com/5DY6ww8.jpg",
            "is_deleted": false,
            "link_url": "http://go/chefdocs",
            "update_date": 1458048163
        },
        {
            "badge_alt": "This badge is awarded to admin who have given a Lunch and Learn presentation",
            "badge_name": "Lunch &#39;n&#39; Learners",
            "create_date": 1437404953,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27939260500,
            "image_url": "http://content.govdelivery.com/attachments/fancy_images/AKDOA/2013/09/219103/229155/lunch-n-learn-small_original_crop.jpg",
            "is_deleted": false,
            "link_url": "https://jira.etsycorp.com/confluence/display/HR/How+to+Lunch+and+Learn",
            "update_date": 1437404953
        },
        {
            "badge_alt": "For those who make badges",
            "badge_name": "Badge-Makers Badge",
            "create_date": 1437752815,
            "datafeed_url": null,
            "flavor_text": "Snaaaake! Snaaaake! Ohhhh it&#39;s a snake.",
            "id": 28011637847,
            "image_url": "https://i.imgur.com/IsBkGUm.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1498240151
        },
        {
            "badge_alt": "A safe laptop is a good laptop. Thank you for getting your laptop checked by Security and CorpIT.",
            "badge_name": "Laptop Healthcheck",
            "create_date": 1438697403,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 28466816121,
            "image_url": "https://i.imgur.com/nv1jP9h.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1438697566
        },
        {
            "badge_alt": "You took the epic journey out to beautiful sunny Secaucus, NJ to visit one of our datacenters!",
            "badge_name": "Datacenter Wizard",
            "create_date": 1437702713,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27983256371,
            "image_url": "https://i.imgur.com/CRhxup2.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1506021086
        },
        {
            "badge_alt": "You touch the F5s.  That can (should?) be scary.",
            "badge_name": "F5 Wrangler",
            "create_date": 1437688022,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27973621163,
            "image_url": "https://i.imgur.com/oa4gBJi.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1481922221
        },
        {
            "badge_alt": "Using vim is it&#39;s own reward, but you still deserve a medal",
            "badge_name": "Vim",
            "create_date": 1437403904,
            "datafeed_url": null,
            "flavor_text": null,
            "id": 27822942841,
            "image_url": "https://i.imgur.com/1owm1jW.png",
            "is_deleted": false,
            "link_url": null,
            "update_date": 1437403904
        },
        {
            "badge_alt": "This is for everyone who has pushed code.",
            "badge_name": "EtsyWeb",
            "create_date": 1437156086,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 27723375281,
            "image_url": "https://i.imgur.com/706zIx4.png",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1564156829
        }
    ],
    "birthday": "",
    "cell_phone": "6314088045",
    "department": "Infrastructure and Operations",
    "department_id": 0,
    "dept": "Technology - Security",
    "desk_phone": "",
    "email": "ngaffey@etsy.com",
    "employee_type": "Regular",
    "enabled": 1,
    "first_name": "Nuala",
    "full_name": "Nuala Gaffey",
    "fulltime_date": 0,
    "gender": "",
    "github": "nuala33",
    "group": "",
    "home_phone": "",
    "id": 26099105232,
    "irc_nick": "ngaffey",
    "is_manager": true,
    "join_date": 1433808000,
    "last_name": "Gaffey",
    "linkedin": "",
    "location": "",
    "login_name": "nualagaffey",
    "manager_auth_username": "cclark",
    "middle_name": "",
    "name": "Nuala Gaffey",
    "nickname": "",
    "office": "Brooklyn, NY",
    "org": "Cost of Revenue (FSLI)",
    "pager_email": "ngaffey@etsy.com",
    "phonetic_name": "Noo-la",
    "prefix": "",
    "pronouns": "she/her",
    "shop_name": "",
    "short_name": "Nuala",
    "skype": "",
    "slack_id": "U27F4A3F0",
    "slack_nick": "ngaffey",
    "suffix": "",
    "team": "Infrastructure and Operations",
    "teams": [
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "yeezus, security, brennivin",
            "name": "Security",
            "slug": "security",
            "team_location": "117 4th Floor pod 01-015 (NW Corner) - San Jose (Jerry Soung) - Chicago (Adam Enger) - San Diego (Patricio Jara)"
        },
        {
            "irc_channel": "security",
            "irc_channel_alert_word": "netsec-team",
            "name": "Security Research and Operations",
            "slug": "security-research-and-operations",
            "team_location": "117 4th Floor pod 01-015 (NW Corner)"
        },
        {
            "irc_channel": "",
            "irc_channel_alert_word": "",
            "name": "Security Operations Org",
            "slug": "security-operations-org",
            "team_location": "BK HQ 4th floor & 5th floor, Dublin, Hudson & plenty of remote representation"
        }
    ],
    "termination_date": 0,
    "title": "Senior Security Engineer II",
    "twitter": "",
    "user_id": 67678667,
    "workday_employee_id": "1317",
    "zendesk_id": 0
}
"Infrastructure and Operations"
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"  | moire
zsh: command not found: moire
Traceback (most recent call last):
  File "request.py", line 44, in <module>
    main()
  File "request.py", line 41, in main
    operator()
  File "request.py", line 37, in operator
    filtering(git_url)
  File "request.py", line 22, in filtering
    print(json.dumps(json_data, indent=4, sort_keys=True)) ## printing out the file in json format.
BrokenPipeError: [Errno 32] Broken pipe
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"  | more 
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
praghav@6622 Chef % vim request.py                                                                            
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"  | more
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
{
    "auth_username": "ngaffey",
    "avatar": "https://i.etsystatic.com/ist/2d2016/2246720043/ist_fullxfull.2246720043_ihv9vo4q.jpg?version=0",
    "badges": [
        {
            "badge_alt": "This badge is awarded to past and present members of the Brooklyn office&#39;s farm share program! ",
            "badge_name": "Local Roots NYC",
            "create_date": 1535043147,
            "datafeed_url": null,
            "flavor_text": "Alexa, how do I cook kohlrabi?",
            "id": 389928128051,
            "image_url": "https://cdn.shopify.com/s/files/1/1812/9769/files/Local_Roots_Logo_Final_Web_280x@2x.png?v=1519679209",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1541701591
        },
        {
            "badge_alt": "Badge of appreciation for speakers who have welcomed new hires at the Eng Onboarding Lightning Talks",
            "badge_name": "Eng Onboarding Lightning Talks",
            "create_date": 1569358386,
            "datafeed_url": null,
            "flavor_text": "",
            "id": 618614020664,
            "image_url": "https://image.freepik.com/free-photo/yellow-electric-lightning-bolt-icon_53876-74655.jpg",
            "is_deleted": false,
            "link_url": "",
            "update_date": 1569572097
        },
        {
            "badge_alt": "Thank you for helping during our on-boarding session. We appreciate you.",
            "badge_name": "Onboarding Helper",
            "create_date": 1565717083,
            "datafeed_url": null,
            "flavor_text": "You are a unicorn WOOP WOOP",
            "id": 588523834498,
            "image_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "is_deleted": false,
            "link_url": "http://imgshare.etsycorp.com/jbarretoetsy-image-share-upload.eux9mr3I.png",
            "update_date": 1569953561
        },
        {
            "badge_alt": "For all the wonderful visitors to the Dublin office",
            "badge_name": "I visited the Dublin office",
            "create_date": 1455897522,
            "datafeed_url": null,
            "flavor_text": "",
praghav@6622 Chef % vim request.py                                                                                 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"  | more
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
"ngaffey"
"Infrastructure and Operations"
...skipping...
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
"ngaffey"
"Infrastructure and Operations"
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"        
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
"ngaffey"
"Infrastructure and Operations"
praghav@6622 Chef % clear

praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey"        
------------------------------------------------------------
SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
------------------------------------------------------------
SPECIAL CREDITS  :- NUALA GAFFEY
 ************************************************************
                                                             
"ngaffey"
"Infrastructure and Operations"
praghav@6622 Chef % vim art.text
praghav@6622 Chef % vim request.py 
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
"ngaffey"
"Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
Name:- "ngaffey"
Team:- "Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 12
    print (".
            ^
SyntaxError: EOL while scanning string literal
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 12
    print (".
            ^
SyntaxError: EOL while scanning string literal
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 12
    print ("
           ^
SyntaxError: EOL while scanning string literal
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 
  File "request.py", line 12
    print ("
           ^
SyntaxError: EOL while scanning string literal
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 

				 ───▄████▄─────
				 ──███▄█▀──────
				 ─▐████──█──█──
				 ──█████▄──────
				 ───▀████▀─────
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
Name:- "ngaffey"
Team:- "Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 

						 ───▄████▄─────
				 		 ──███▄█▀──────
						 ─▐████──█──█──
						 ──█████▄──────
						 ───▀████▀─────
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
Name:- "ngaffey"
Team:- "Infrastructure and Operations"
praghav@6622 Chef % vim request.py                                                                          
praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 

					 ───▄████▄─────
				 	 ──███▄█▀──────
					 ─▐████──█──█──
					 ──█████▄──────
					 ───▀████▀─────
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
Name:- "ngaffey"
Team:- "Infrastructure and Operations"
praghav@6622 Chef % clear

praghav@6622 Chef % python3.8 request.py --url "https://datafeeds.etsycorp.com/staff?auth_username=ngaffey" 

					 ───▄████▄─────
				 	 ──███▄█▀──────
					 ─▐████──█──█──
					 ──█████▄──────
					 ───▀████▀─────
               -----------------------------------------------------------------
                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.
               -----------------------------------------------------------------
                              SPECIAL CREDITS  :- NUALA GAFFEY
                 ************************************************************
                                                                                
Name:- "ngaffey"
Team:- "Infrastructure and Operations"
praghav@6622 Chef % cler
zsh: command not found: cler
praghav@6622 Chef % clear



































praghav@6622 Chef % vim request.py 
praghav@6622 Chef % vim request.py 



















































#!/usr/bin/env python
  
import json
import pprint
import requests
from optparse import OptionParser
import sys
import re

def usage():

        print ("""
                                         ───▄████▄─────
                                         ──███▄█▀──────
                                         ─▐████──█──█──
                                         ──█████▄──────
                                         ───▀████▀─────""")
        print ("               -----------------------------------------------------------------")
        print ("                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.")
        print ("               -----------------------------------------------------------------")
        print ("                              SPECIAL CREDITS  :- NUALA GAFFEY")
        print ("                 ************************************************************")
        print ("                                                                                ")

def filtering(git_url):

        response = requests.get(git_url)
        json_data = response.json()
        #print(json.dumps(json_data, indent=4, sort_keys=True)) ## printing out the file in json format.
        u_name = json.dumps(json_data["auth_username"])
        print ("Name:-",u_name)
        u_team = json.dumps(json_data["team"])
        print ("Team:-",u_team)

def operator():

        git_url = ""
        parser = OptionParser()
        parser.add_option('-u','--url', dest = 'git_url', type ='string',help = 'Specify a  datafeed url of etsy')
        (options,args) = parser.parse_args()
        git_url = options.git_url
        if git_url == None:
                print (parser.usage)
                exit(0)
        else:
                filtering(git_url)

def main():
      usage()
      operator()

if __name__=='__main__':
"request.py" 54L, 1755C
