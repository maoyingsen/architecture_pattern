from compare import sync

def test_when_a_file_exists_in_the_source_but_not_the_destination_2():
    src_hashes = {'hash1': 'fn1'}
    dst_hashes = {}
    expected_action = [('COPY', '/src/fn1', '/dst/fn1')]
    res = sync(src_hashes, dst_hashes, '/src', '/dst')

    assert res == expected_action

def test_when_a_file_has_been_renamed_in_the_source_2():
    src_hashes = {'hash1': 'fn1'}
    dst_hashes = {'hash1': 'fn2'}
    expected_action = [('RENAME', '/dst/fn2', '/dst/fn1')]

    res = sync(src_hashes, dst_hashes, '/src', '/dst')

    assert res == expected_action

def test_when_a_file_in_dest_but_not_in_src_and_verse_vice():
    src_hashes = {'hash10': 'fn1', 'hash1': 'fn3'}
    dst_hashes = {'hash1': 'fn2', 'hash111': 'fn111'}

    expected_action = [('COPY', '/src/fn1', '/dst/fn1'), ('REMOVE', '/dst/fn111'), ('RENAME', '/dst/fn2', '/dst/fn3')]   

    res = sync(src_hashes, dst_hashes, '/src', '/dst')
    #res =  [ ('RENAME', '/dst/fn2', '/dst/fn3'), ('COPY', '/src/fn1', '/dst/fn1'), ('REMOVE', '/dst/fn111')]   
    assert res.sort() == expected_action.sort()