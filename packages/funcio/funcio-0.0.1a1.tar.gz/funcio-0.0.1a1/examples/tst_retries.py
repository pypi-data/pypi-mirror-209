import asyncio

from retry import retry


#region Retry context in global scope
# counter1 = 0
#
# with retry(3):
#     print(f'Run {counter1}')
#     counter1 += 1
#     if counter1 < 4:
#         raise Exception(f'Test exception {counter1}')
#     print('Run completed')
#
# print(f'counter: {counter1}')
# if counter1 == 4:
#     print('Success')
# else:
#     print('Fail')

#endregion


#region Retry context in function scope
# counter2 = 0
#
#
# def run():
#     global counter2
#     with retry(3):
#         print(f'Run {counter2}')
#         counter2 += 1
#         if counter2 < 4:
#             raise Exception(f'Test exception {counter2}')
#         print('Run completed')
#
#     print('Done')
#
#
# run()
# print(f'counter: {counter2}')
# if counter2 == 4:
#     print('Success')
# else:
#     print('Fail')

#endregion


#region Retry context in closure scope
counter3 = 0


def outer():
    counter3 = 0
    def inner():
        # global counter3
        nonlocal counter3
        with retry(3):
            print(f'Run {counter3}')
            counter3 += 1
            if counter3 < 4:
                raise Exception(f'Test exception {counter3}')
            print('Run completed')

    inner()

    print(f'counter: {counter3}')


outer()
print(f'counter: {counter3}')
if counter3 == 4:
    print('Success')
else:
    print('Fail')

#endregion


#region Retry context assign new variable


def run():
    counter = 0
    with retry(3):
        print(f'Run {counter}')
        counter += 1
        if counter < 4:
            raise Exception(f'Test exception {counter}')
        finish = True
        print('Assign finish = True')

    print(f'counter: {counter}')
    print(f'finish: {finish}')


run()

#endregion


#region Retry context delete variable


# def run():
#     counter = 0
#     foo = None
#     with retry(3):
#         print(f'Run {counter}')
#         counter += 1
#         if counter < 4:
#             raise Exception(f'Test exception {counter}')
#         del foo
#         print('Delete foo')
#
#     print(f'counter: {counter}')
#     print(f'foo: {foo}')
#
#
# run()

#endregion


#region Retry context asynchrony


# async def run():
#     counter = 0
#     async with retry(3):
#         print(f'Run {counter}')
#         counter += 1
#         await asyncio.sleep(0.1)
#         if counter < 4:
#             raise Exception(f'Test exception {counter}')
#         print('Run completed')
#
#     print(f'counter: {counter}')
#
#
# asyncio.run(run())

#endregion

import inspect


# def foo():
#
#     frame = inspect.currentframe()
#     c = 1
#
#     def bar():
#
#         print(frame.f_locals is frame.f_globals)
#
#         frame_locals = frame.f_locals
#         exec('c = 3', frame.f_globals, frame_locals)
#         print(frame_locals['c'])
#         print(frame.f_locals['c'])
#
#     # print(frame.f_locals['d'])
#
#     bar()
#
#
# foo()
