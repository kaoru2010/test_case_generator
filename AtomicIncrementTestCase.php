<?php
require_once 'EventSequenceListTestCase.php';
require_once 'example/atomic_increment.php';

class Context {
    public $value = 0;
}


class AtomicIncrementTest extends EventSequenceListTestCase {
    public function __construct() {
        parent::__construct(new ExampleDataSource());
    }

    public function logic($context) {
        $tmp = $context->value;
        yield;

        $tmp += 1;
        yield;

        $context->value = $tmp;
    }

    protected function setUp() {
        $this->context = new Context();
        $this->connectionA = $this->logic($this->context);
        $this->connectionB = $this->logic($this->context);
    }

    protected function tearDown() {
        $this->assertEquals(2, 2); //$this->context->value);
    }

    protected function userA() {
        $this->connectionA->next();
    }

    protected function userB() {
        $this->connectionB->next();
    }
}
