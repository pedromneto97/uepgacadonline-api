package com.pstwh.uepgacadonline_android;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import java.io.File;

public class DocumentActivity extends AppCompatActivity {

    public UepgWrapper uepg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_document);

        Intent intent = getIntent();
        uepg = (UepgWrapper) intent.getSerializableExtra("uepg");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_documents, menu);

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.menu_item_notas:
                Intent grades = new Intent(DocumentActivity.this, GradeActivity.class);
                grades.putExtra("uepg", uepg);
                startActivity(grades);
                break;
        }

        return super.onOptionsItemSelected(item);
    }
}
