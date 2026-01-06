package com.message;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MessageAppTest {

    @Test
    void verifyMessage() {
        assertEquals(
            "Learning DevOps step by step makes life easier!",
            MessageApp.getMessage()
        );
    }
}
