package com.pstwh.uepgacadonline_android;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.custom_toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplayShowHomeEnabled(true);

        final EditText ra = (EditText) findViewById(R.id.ra_edit_text);
        final EditText password = (EditText) findViewById(R.id.password_edit_text);


        final Button login = (Button) findViewById(R.id.login_button);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                UepgWrapper uepg = new UepgWrapper(ra.getText().toString(), password.getText().toString());

                Intent authenticate = new Intent(MainActivity.this, GradeActivity.class);
                authenticate.putExtra("uepg", uepg);

                startActivity(authenticate);
            }
        });

        final ImageView github = (ImageView) findViewById(R.id.github_image_view);
        github.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent viewIntent =
                        new Intent("android.intent.action.VIEW",
                                Uri.parse("https://github.com/pstwh/uepgacadonline-android"));
                startActivity(viewIntent);
            }
        });
    }
}
