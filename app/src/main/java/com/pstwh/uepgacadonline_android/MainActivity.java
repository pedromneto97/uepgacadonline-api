package com.pstwh.uepgacadonline_android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText ra = (EditText) findViewById(R.id.ra_edit_text);
        final EditText password = (EditText) findViewById(R.id.password_edit_text);


        final Button login = (Button) findViewById(R.id.login_button);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Scrapper scrapper = new Scrapper(ra.getText().toString(), password.getText().toString());
                scrapper.getGrade();
            }
        });
    }
}
