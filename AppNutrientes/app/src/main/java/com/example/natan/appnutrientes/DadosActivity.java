package com.example.natan.appnutrientes;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class DadosActivity extends AppCompatActivity {

    EditText editAltura;
    EditText editPeso;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dados);

        final Intent intent = getIntent();

        String nome = intent.getStringExtra("Nome");
        TextView nomeDados = findViewById(R.id.Nome);
        editAltura = findViewById(R.id.Altura);
        editPeso = findViewById(R.id.Peso);
        nomeDados.setText(nome + "\nDigite os dados a seguir");
    }

    public void finalizar(View view) {
        int altura = Integer.parseInt(editAltura.getText().toString());
        double peso = Double.parseDouble(editPeso.getText().toString());

        Intent intent = new Intent();

        intent.putExtra("Altura", altura);
        intent.putExtra("Peso", peso);

        setResult(RESULT_OK, intent);

        finish();
    }
}
