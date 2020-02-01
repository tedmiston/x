import os.path

import yaml
from invoke import task

@task
def setup(ctx):
    """load tasks from yaml file"""
    with open('tasks.yaml') as fp:
        contents = yaml.load(fp, Loader=yaml.FullLoader)
    ctx.yaml_tasks = contents['tasks']

@task(pre=[setup])
def run_task(ctx, id):
    task = ctx.yaml_tasks[id]
    pre, task_, post = task.get('pre'), task['task'], task.get('post')
    if pre: ctx.run(os.path.expandvars(pre))
    ctx.run(os.path.expandvars(task['task']))
    if post: ctx.run(os.path.expandvars(post))

@task(pre=[setup])
def hello(ctx):
    """hello world 1"""
    run_task(ctx, 'hello')

@task(pre=[setup])
def world(ctx):
    """hello world 2"""
    run_task(ctx, 'world')

@task(pre=[setup])
def add(ctx):
    """add two numbers from environment variables"""
    run_task(ctx, 'add')
