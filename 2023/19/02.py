wfs, pts = open('input').read().split('\n\n')

workflows = {}
for wf in wfs.split('\n'):
    key, wf = wf.strip().split('{')
    workflows[key] = wf[:-1].split(',')

workflows['A'] = ['A']
workflows['R'] = ['R']

accepts = []

def execute_workflow(workflow_key, bounds):
    workflow = workflows[workflow_key]
    for rule in workflow:
        if rule == 'A':
            accepts.append(bounds)
            return
        if rule == 'R':
            return
        if rule in workflows:
            execute_workflow(rule, bounds)
            return

        check, next_workflow = rule.split(':')
        if '<' in check:
            key, val = check.split('<')
            nb = bounds.copy()
            nb[key] = (nb[key][0], int(val) - 1)
            bounds[key] = (int(val), bounds[key][1])
        elif '>' in check:
            key, val = check.split('>')
            nb = bounds.copy()
            nb[key] = (int(val) + 1, nb[key][1])
            bounds[key] = (bounds[key][0], int(val))

        execute_workflow(next_workflow, nb)


execute_workflow('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

total = 0
for accept in accepts:
    x, m, a, s = accept['x'], accept['m'], accept['a'], accept['s']
    total += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)

print(total)
