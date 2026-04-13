---
name: Bug Template
type: bug-fix
date: YYYY-MM-DD
project: brantham
---

# [Bug Title]

**Date Fixed**: YYYY-MM-DD  
**Severity**: Low | Medium | High | Critical  
**Component**: [Code location / system]  
**Status**: Fixed | Monitoring

## Problem

[What was broken? How did it manifest? Customer impact?]

## Root Cause

[Why did it happen? Investigation details?]

## Fix Applied

[What code changed? File paths + line numbers]

```python
# Before
old_code()

# After
new_code()
```

## Testing

- [x] Added test case
- [x] Verified in staging
- [x] Verified in production

## Prevention

[How do we prevent this class of bugs in future? New pattern? New test?]

## Related

- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/patterns/PATTERN_NAME|Pattern Created from This Bug]]
