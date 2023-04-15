from indico.modules.events import Event
from indico.modules.categories import Category


def build_event_dict(events):
    events_dict = {}
    for event in events:
        event_details = Event.get(event)
        category = Category.get(event_details.category_id)
        events_dict[event] = {}
        events_dict[event]['title'] = event_details.title
        events_dict[event]['start_dt'] = event_details.start_dt.astimezone(
            event_details.display_tzinfo)
        events_dict[event]['end_dt'] = event_details.end_dt.astimezone(
            event_details.display_tzinfo)
        events_dict[event]['categories'] = {}
        events_dict[event]['categories'][1] = {"id": category.id, "title": category.title}
        if not category.is_root:
            order = 2
            while True:
                parent_category = Category.get(category.parent_id)
                events_dict[event]["categories"][order] = {"id": parent_category.id,
                                                           "title": parent_category.title}
                category = Category.get(parent_category.id)
                order += 1
                if category.is_root:
                    break
    return events_dict
