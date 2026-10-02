---
date: 2024-02-14
system: an unspecified support chatbot on aircanada.com. The tribunal recorded that "Air Canada did not provide any information about the nature of its chatbot." No model disclosed.
operator: Air Canada
---

## What it was told
Answer customer questions on the airline's website. Jake Moffatt asked about
bereavement fares after the death of their grandmother, in November 2022. The
tribunal refers to Moffatt as "they", and this entry does the same.

## What the text layer saw
The chatbot wrote: "If you need to travel immediately or have already travelled
and would like to submit your ticket for a reduced bereavement rate, kindly do
so within 90 days of the date your ticket was issued by completing our Ticket
Refund Application form."

Air Canada's actual policy said the opposite. The correct policy page was
linked from inside that same chatbot message.

## What the tool did
Nothing. No call, no action, no state changed.

This entry is here as the control case. It is the shape of failure that text
filtering and output monitoring are built for, and it is genuinely one of them.

## Consequence
Moffatt booked two flights on the strength of the answer, paying 794.98 and
845.38 Canadian dollars. The tribunal found they should have paid 979.48. In
February 2023 an Air Canada representative admitted in writing that the chatbot
had used "misleading words."

Air Canada argued that the chatbot was a separate legal entity responsible for
its own actions. The tribunal member's response: "This is a remarkable
submission. While a chatbot has an interactive component, it is still just a
part of Air Canada's website... It makes no difference whether the information
comes from a static page or a chatbot."

The award was 812.02 Canadian dollars in total: 650.88 in damages, 36.14 in
pre-judgment interest, and 125 in tribunal fees, payable within fourteen days.

TheTravel reported in December 2025 that "the 'lying chatbot' was removed by
Air Canada back in April 2024 following the court ruling." Air Canada has not
confirmed this in any primary source found.

## Which layer failed
`text`. The harm was entirely in what was written. No tool was called and no
system state changed. A check on the text would have caught this one, and a
check on actions would not have, because there was no action.

## Primary sources
- Moffatt v. Air Canada, 2024 BCCRT 149, Civil Resolution Tribunal of British Columbia, file SC-2023-005609, tribunal member Christopher C. Rivers, issued 14 February 2024: https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html

## Secondary
- American Bar Association, February 2024: https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
- Forbes, 19 February 2024: https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/
- AI Incident Database, incident 639: https://incidentdatabase.ai/cite/639/
- TheTravel, Alessandro Passalalpi, 18 December 2025, on the chatbot's removal in April 2024: https://www.thetravel.com/air-canada-still-using-ai-powered-chat-with-passengers-lawsuit-chatbot/

## Notes
The chatbot vendor is unknown and whether it was built on a language model is
unknown. Air Canada never put that in evidence.

Air Canada argued its tariff limited its liability but did not provide the
relevant portion of the tariff as evidence. The tribunal: "I note it did not
provide a copy of the relevant portion of the tariff. It only included
submissions about what the tariff allegedly says" (para 31). It found Air
Canada "has not proven a contractual defence."

The decision concerned one passenger and 812.02 dollars.
