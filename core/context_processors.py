def site_context(request):
    """
    Context processor to add site-wide information to all templates.
    """
    # Get current path to determine active navigation item
    current_path = request.path.strip('/')
    
    # Define navigation items with their URLs and labels
    nav_items = [
        {'url': 'how-it-works/', 'label': 'How It Works', 'name': 'how_it_works'},
        {'url': 'pricing/', 'label': 'Pricing', 'name': 'pricing'},
        {'url': 'faq/', 'label': 'FAQ', 'name': 'faq'},
        {'url': 'testimonials/', 'label': 'Testimonials', 'name': 'testimonials'},
        {'url': 'contact/', 'label': 'Contact', 'name': 'contact'},
    ]
    
    # Mark the active navigation item
    for item in nav_items:
        if current_path == item['url'].rstrip('/'):
            item['active'] = True
        else:
            item['active'] = False
    
    return {
        'site_name': 'TrueDNA',
        'site_tagline': 'Discreet DNA Testing. Real Peace of Mind.',
        'company_phone': '+233 XXXXXXXX',
        'company_email': 'support@truedna.com',
        'company_whatsapp': '233XXXXXXXXX',
        'nav_items': nav_items,
        'social_links': {
            'facebook': 'https://facebook.com/truednagh',
            'instagram': 'https://instagram.com/truedna_ghana',
            'twitter': 'https://twitter.com/truedna_ghana',
        },
        'business_hours': {
            'monday_friday': '8:00 AM - 6:00 PM',
            'saturday': '9:00 AM - 3:00 PM',
            'sunday': 'Closed',
        },
        'pricing': {
            'peace_of_mind': 450,
            'peace_of_mind_display': 'GHS 450',
            'legal_dna': 850,
            'legal_dna_display': 'GHS 850',
        },
        'footer_links': [
            {'url': 'privacy/', 'label': 'Privacy Policy'},
            {'url': 'terms/', 'label': 'Terms of Service'},
            {'url': 'contact/', 'label': 'Contact Us'},
        ]
    }
