# Remotion Opaque Fallback Failure

Failure: a user-confirmed Remotion transparent foreground returns a white-background PNG and C-line marks it complete by downgrading Alpha to opaque.

Why it fails: the asset cannot serve as a compositable foreground. Return `alpha_generation_failure` after the allowed local revisions; do not deliver it.
