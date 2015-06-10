def generate_test(index, labels, data):
    def test(self):
        for event_id in data[index]:
            method = getattr(self, labels[event_id])
            method()

    return test

def _event_sequence_test_impl(labels, data):
    def _(clazz):
        for i in range(0, len(data)):
            test_name = 'test_%s' % ('_'.join([labels[x] for x in data[i]]))
            test = generate_test(i, labels, data)
            setattr(clazz, test_name, test)
        return clazz
    return _

def event_sequence_test(data_source):
    return _event_sequence_test_impl(data_source.getLabels(), data_source.getData())

def event_sequence_test_raw(data_source):
    return _event_sequence_test_impl(data_source['labels'], data_source['data'])
