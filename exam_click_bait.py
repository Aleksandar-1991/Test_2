from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = [int(x) for x in input().split()]
target_engagement = int(input())
final_feed = list()

greater_el = int()
smaller_el = int()
greater_el_origin = str()

while suggested_links and featured_articles:
    el_suggested_links = suggested_links.popleft()
    el_featured_articles = featured_articles.pop()

    if el_suggested_links > el_featured_articles:
        greater_el = el_suggested_links
        smaller_el = el_featured_articles
        greater_el_origin = "Suggested Links"
    elif el_featured_articles >el_suggested_links:
        greater_el = el_featured_articles
        smaller_el = el_suggested_links
        greater_el_origin = "Featured Articles"
    else:
        final_feed.append(0)
        continue

    remainder =  greater_el % smaller_el
    if greater_el_origin == "Featured Articles":
        final_feed.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)
        else:
            continue
    elif greater_el_origin == "Suggested Links":
        negative_remainder = (abs(remainder)) * (-1)
        final_feed.append(negative_remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)
        else:
            continue


print(f"Final Feed: {(', '.join([str(el) for el in final_feed]))}")
total_engagement = sum(final_feed)
if total_engagement >= target_engagement:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
else:
    shortfall = target_engagement - total_engagement
    print(f"Goal not achieved! Short by: {shortfall}")


