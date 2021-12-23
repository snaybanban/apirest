<template>
  <q-page class="flex flex-center">
     <div class="q-pa-md">
      <q-table
        title="Treats"
        :rows="rows"
        :columns="columns"
        row-key="name"
    />
  </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageIndex',
  data() {
    return {
      columns: [
        {
          name: 'nombre',
          required: true,
          label: 'Nombre',
          align: 'left',
          field: 'nombre',
          sortable: true
        },
        {
          name: 'apellido',
          required: true,
          label: 'Apellido',
          align: 'center',
          field: 'apellido',
          sortable: true
        },
        {
          name: 'edad',
          required: true,
          label: 'Edad',
          align: 'center',
          field: 'edad',
          sortable: true
        },
        {
          name: 'email',
          required: true,
          label: 'Correo',
          align: 'center',
          field: 'email',
          sortable: true
        },
        {
          name: 'telefono',
          required: true,
          label: 'Telefono',
          align: 'center',
          field: 'telefono',
          sortable: true
        },
        {
          name: 'direccion',
          required: true,
          label: 'Direccion',
          align: 'center',
          field: 'direccion',
          sortable: true
        },
      ],
      rows: [],
    };
  },
mounted() {
  this.getRows();
  },
methods: {
  getRows(){
    this.$axios.get('http://127.0.0.1:8080/api/persona/').then(response => {
      this.rows = response.data;
    })
    .catch(error => {
      console.log(error);
    });
  }
  }
});

</script>
