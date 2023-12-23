wfs, pts = open('input').read().split('\n\n')

workflows = {}
for wf in wfs.split('\n'):
    key, wf = wf.strip().split('{')
    workflows[key] = wf[:-1].split(',')

parts = []
for pt in pts.split('\n'):
    pt = [xmas.split('=') for xmas in [xmas for xmas in pt[1:-1].split(',')]]
    parts.append({xmas[0]: int(xmas[1]) for xmas in pt})

def execute_workflow(workflow_key, part):
    workflow = workflows[workflow_key]
    for rule in workflow:
        if rule == 'A':
            return True
        if rule == 'R':
            return False
        if rule in workflows:
            return execute_workflow(rule, part)

        done = False
        check, outcome = rule.split(':')
        if '<' in check:
            key, val = check.split('<')
            done = part[key] < int(val)
        elif '>' in check:
            key, val = check.split('>')
            done = part[key] > int(val)

        if done:
            if outcome == 'A':
                return True
            elif outcome == 'R':
                return False
            else:
                return execute_workflow(outcome, part)


print(sum(sum(part.values()) for part in parts if execute_workflow('in', part)))
