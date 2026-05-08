
class SmartCopyEngine:
    @staticmethod
    def symptoms(symptoms):
        if not symptoms: return ""
        # Professional clinical formatting
        cleaned = [s.replace('_', ' ').lower() for s in symptoms]
        if len(cleaned) == 1:
            res = cleaned[0]
        elif len(cleaned) == 2:
            res = f"{cleaned[0]} and {cleaned[1]}"
        else:
            res = ", ".join(cleaned[:-1]) + f", and {cleaned[-1]}"
        return res.capitalize() + "."

    @staticmethod
    def medications(meds):
        if not meds: return ""
        lines = []
        for m in meds:
            if isinstance(m, tuple):
                name = m[0]
            elif isinstance(m, dict):
                name = m.get("name", str(m))
            else:
                name = str(m)
            lines.append(f"- {name.title()}")
        return "Suggested Medications:\n" + "\n".join(lines)

    @staticmethod
    def tests(tests):
        if not tests: return ""
        lines = []
        for t in tests:
            if isinstance(t, tuple):
                name, _, priority = t
                lines.append(f"- {name} ({priority})")
            elif isinstance(t, dict):
                name = t.get("name", str(t))
                lines.append(f"- {name}")
            else:
                lines.append(f"- {str(t)}")
        return "Recommended Workup:\n" + "\n".join(lines)

    @staticmethod
    def billing(codes):
        if not codes: return ""
        lines = []
        for c in codes:
            if isinstance(c, tuple):
                code, desc, _ = c
                lines.append(f"- {desc} [{code}]")
            else:
                lines.append(f"- {str(c)}")
        return "Billing/Coding:\n" + "\n".join(lines)

    @staticmethod
    def differential(suggestions):
        if not suggestions: return ""
        return "Differential Considerations:\n" + "\n".join(f"- {s}" for s in suggestions)
