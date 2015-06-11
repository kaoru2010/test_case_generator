<?php
abstract class EventSequenceListTestCase extends PHPUnit_Framework_TestCase
{
    public function __construct(Traversable $dataSource) {
        $this->_dataSource = $dataSource;
    }

    /**
     * @dataProvider provideDataSource
     */
    public function testEventSequence()
    {
        foreach (func_get_args() as $event) {
            $this->{$event}();
        }
    }

    public function provideDataSource() {
        return $this->_dataSource;
    }
}
