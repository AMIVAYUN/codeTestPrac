#include <jni.h>
#include <stdio.h>
#include "JNI_Helloworld.h" // 패키지명을 포함한 헤더 파일

// JNI function implementation
JNIEXPORT void JNICALL Java_JNI_Helloworld_printHelloWorld(JNIEnv *env, jobject obj) {
    printf("Hello, World from JNI!\n");
}

