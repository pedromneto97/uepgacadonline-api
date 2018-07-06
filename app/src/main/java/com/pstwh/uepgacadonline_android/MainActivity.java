package com.pstwh.uepgacadonline_android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Scrapper scrapper = new Scrapper("14147326", "");
        scrapper.getGrade();


        setContentView(R.layout.activity_main);
    }
}
