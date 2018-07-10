package com.pstwh.uepgacadonline_android;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

import com.pstwh.uepgacadonline_android.helpers.PerfilFormHelper;
import com.pstwh.uepgacadonline_android.models.Perfil;

import java.util.concurrent.ExecutionException;

public class PerfilActivity extends AppCompatActivity {

    public UepgWrapper uepg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perfil);

        Intent intent = getIntent();
        uepg = (UepgWrapper) intent.getSerializableExtra("uepg");

        try {
            Perfil perfil = uepg.getPerfil();
            PerfilFormHelper helper = new PerfilFormHelper(PerfilActivity.this);

            helper.setPerfil(perfil);
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_grades, menu);

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.menu_item_contributors:
                Intent contributors = new Intent(PerfilActivity.this, ContributorsActivity.class);
                startActivity(contributors);
                break;

            case R.id.menu_item_perfil:
                Intent grade = new Intent(PerfilActivity.this, GradeActivity.class);
                grade.putExtra("uepg", uepg);
                startActivity(grade);
                break;
        }

        return super.onOptionsItemSelected(item);
    }
}
