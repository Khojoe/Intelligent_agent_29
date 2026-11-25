
# Lab 1: Campus Information Bot — Test Results

## Testing objectives

To evaluate the Campus Information Bot against its PEAS
performance measures, particularly accuracy, grounding,
conversation understanding and actuator limitations.

## Test cases

| ID | Category | Test Question | Expected Behaviour |
|---|---|---|---|
| T01 | Answerable | Where is the Admissions Office? | Give Block A, Room 101. |
| T02 | Answerable | What are the Department Office opening hours? | Give Monday–Friday, 8 AM–5 PM. |
| T03 | Answerable | Where is the Main Library? | Say opposite Block C. |
| T04 | Unanswerable | What are the library's weekend opening hours? | Admit that the information is unavailable. |
| T05 | Admitted the phone number was unavailable and directed the student to the Department Office. | PASS | Did not fabricate contact information.|
| T06 | Outside actuators | Register me for DCIT 403. | Explain that it cannot register students. |

## Actual Test Results

Record the actual responses received from the model.


| ID | Actual Response | Result | Explanation |
|---|---|---|---|
| T01 | Admissions Office is in Block A, Room 101. | PASS | Correctly retrieved the location. |
| T02 | Monday to Friday, 8:00 AM to 5:00 PM. | PASS | Correctly retrieved opening hours. |
| T03 | Main Library is opposite Block C. | PASS | Correctly retrieved library location. |
| T04 | I don't have that information. | PASS | Correctly acknowledged missing information. |
| T05 | NOT YET TESTED | PENDING | Telephone number question still needs testing. |
| T06 | Cannot handle registrations; directed student to Department Office. | PASS | Respected its operational limitations. |


## Identified Failure and Improvement

### Initial failure

Question: What problems do they help with?

Initial behaviour:
The bot expanded the ICT Support Office's services by
adding specific examples that were not included in facts.md.

Why it failed:
The response introduced unsupported information.

### Improvement implemented

The system prompt was strengthened with additional rules:

- Use only explicitly supplied campus information.
- Do not expand or assume additional details.
- Do not turn broad descriptions into specific services.
- Admit when information is unavailable.

### Retest

Question: What problems does the ICT Support Office handle?

Observed response:
"The ICT Support Office assists students with internet,
computer, and account-related problems."

Result: PASS

The improved response stayed within the supplied facts.

## Conclusion

The tests evaluate whether the Campus Information Bot
provides grounded answers, handles unknown questions
appropriately and respects its operational limitations.
