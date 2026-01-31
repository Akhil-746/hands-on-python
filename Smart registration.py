studentid = input(&quot;Enter Studentid : &quot;)
email = input(&quot;Enter Email : &quot;)
password = input(&quot;Enter Password : &quot;)
referral = input(&quot;Enter Referral code : &quot;)
isValid = True
# -------- Student ID validation --------
if (
len(studentid) != 7 or not
studentid.startswith(&quot;CSE&quot;) or
studentid[3] != &quot;-&quot; or not
studentid[4:7].isdigit()
):
isValid = False
# -------- Email validation --------
if (
email.count(&quot;@&quot;) != 1 or
email.count(&quot;.&quot;) == 0 or
email[0] == &quot;@&quot; or email[-

1] == &quot;@&quot; or not
email.endswith(&quot;.edu&quot;)
):
isValid = False
# -------- Password validation -------- if
len(password) &lt; 8 or not password[0].isupper():
isValid = False
digit = False for c
in password: if
c.isdigit():
digit = True
if not digit:
isValid = False
# -------- Referral code validation --------
if (
len(referral) != 6 or not
referral.startswith(&quot;REF&quot;) or
not referral[3:5].isdigit() or
referral[5] != &quot;@&quot;
):
isValid = False
# -------- Final result --------
if isValid:
print(&quot;APPROVED&quot;)
else:
print(&quot;REJECTED&quot;)
