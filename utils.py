from jinja2 import Template

file = open('email_templates/listings.html', 'r')
markdown = file.read()
file.close()
listing_template = Template(markdown)


def create_listings_message(listings):
    message = listing_template.render(cars=listings)
    return message
