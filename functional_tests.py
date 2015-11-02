from selenium import webdriver
browser = webdriver.Firefox()
# Edith has heard about a cool new inline to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')
# She notices the page title and header mention todo lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item right away

# She types "Buy Peacock Feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a todo list

# There is still a text box inviting her to add another item. She
# enters "Use Peacock feathers to make a fly" (Edith is very methodological)

# The page updates again, and now shows both her items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits the URL - her to-do list is still there.

# Satisfied, she goes back to sleep.

browser.quit()

