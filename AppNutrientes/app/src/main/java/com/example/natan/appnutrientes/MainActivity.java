package com.example.natan.appnutrientes;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import javax.xml.transform.Templates;

public class MainActivity extends AppCompatActivity {
    EditText editNome;
    TextView textAltura;
    TextView textPeso;
    TextView dados;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editNome = (EditText) findViewById(R.id.Nome);
        textAltura = (TextView) findViewById(R.id.Altura);
        textPeso = (TextView) findViewById(R.id.Peso);
        dados = (TextView) findViewById(R.id.dados);
        Spinner spinner = (Spinner) findViewById(R.id.spinner);
        // Create an ArrayAdapter using the string array and a default spinner layout
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.planets_array, android.R.layout.simple_spinner_item);
        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);
    }

    public void dados(View view) {
        String nome = editNome.getText().toString();
        final Intent intent = new Intent(this, DadosActivity.class);
        intent.putExtra("Nome", nome);
        startActivityForResult(intent,1);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 1){
            if (resultCode == RESULT_OK){
                double altura = data.getDoubleExtra("Altura",0);
                double peso = data.getDoubleExtra("Peso", 0);
                String nome = data.getStringExtra("Nome");
                textAltura.setText(String.format("Altura: %s", Double.toString(altura)));
                textAltura.setVisibility(View.VISIBLE);
                textPeso.setText(String.format("Peso: %s", Double.toString(peso)));
                textPeso.setVisibility(View.VISIBLE);
                dados.setText(String.format("Dados de %s", nome));
                dados.setVisibility(View.VISIBLE);
                editNome.getText().clear();

            }
        }

    }
}
