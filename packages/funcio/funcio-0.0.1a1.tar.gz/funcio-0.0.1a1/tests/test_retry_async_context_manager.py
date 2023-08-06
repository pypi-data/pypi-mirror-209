import pytest

from funcio import retry


@pytest.mark.asyncio
async def test_retry():
    first = True
    async with retry():
        if first:
            first = False
            raise ValueError('test')


@pytest.mark.asyncio
async def test_raise_exception():
    with pytest.raises(ValueError):
        async with retry(1):
            raise ValueError('test')


@pytest.mark.asyncio
async def test_create_local_variable():
    first = True
    async with retry(1):
        if first:
            first = False
            raise ValueError('test')
        flag = True

    assert flag is True


@pytest.mark.asyncio
async def test_update_local_variable():
    first = True
    flag = False
    async with retry(1):
        if first:
            first = False
            raise ValueError('test')
        flag = True

    assert flag is True


@pytest.mark.asyncio
async def test_remove_local_variable():
    first = True
    flag = True
    async with retry(1):
        if first:
            first = False
            raise ValueError('test')
        del flag

    assert 'flag' not in locals()


@pytest.mark.asyncio
async def test_awaitable():

    async def foo():
        return True

    first = True
    flag = False
    async with retry():
        if first:
            first = False
            raise ValueError('test')
        await foo()
        flag = True

    assert flag is True
