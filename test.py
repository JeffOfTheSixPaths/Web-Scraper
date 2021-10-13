from Scrap import *
import json
f = open('imp.json')
data = json.load(f)
headline_list = get_page(data["yahoo finance"]["url"]).find_all("h3")
summ = get_summaries(data["yahoo finance"]["url"])



print(rmAngles("<amognus> this is the headline </amongnus>"))
print(rmAngles("<n> <this </n>"))



##   <h3 class="Mb(5px)" data-reactid="25"><a class="js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled" data-reactid="26" data-uuid="6b8edb79-dd65-48ec-b497-3958f011f098" data-wf-caas-prefetch="1" data-wf-caas-uuid="6b8edb79-dd65-48ec-b497-3958f011f098" href="/news/retail-sales-consumer-price-index-what-to-know-this-week-145855567.html"><u class="StretchedBox" data-reactid="27"></u><!-- react-text: 28 -->Retail sales, Consumer Price Index: What to know this week<!-- /react-text --></a></h3>

