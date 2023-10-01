import Header from "../../components/Header";
import { Box, Typography, useTheme } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import { tokens } from "../../theme";
import { mockDataContacts } from "../../data/mockData";

const Contact = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const columns = [
    { field: 'id', headerName: 'ID', flex: 0.5 },
    {
        field: 'registrarId',
        headerName: 'Register ID',
        type: "number",
        flex: 1,
      },
    {
      field: 'name',
      headerName: 'Name',
      flex: 1,
    },
    {
      field: 'age',
      headerName: 'Age',
      type: 'number',
    },
    {
      field: 'phone',
      headerName: 'Phone Number',
      flex: 1,
    },
    {
      field: 'email',
      headerName: 'Email',
      flex: 1,
    },
    {
      field: 'address',
      headerName: 'Address',
      flex: 1,
    },
    {
        field: 'city',
        headerName: 'City',
        flex: 1,
      },
    {
        field: 'zipCode',
        headerName: 'Zip Code',
        flex: 1,
    }
  ];

  return (
      <Box sx={{ height: 400, width: '100%' }}>
        <Header title = "CONTACTS" subtitle="List of Contacts for Future Refrence" />
        <DataGrid
          rows={mockDataContacts}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: {
                pageSize: 5,
              },
            },
          }}
          pageSizeOptions={[5]}
          checkboxSelection
          disableRowSelectionOnClick
        />
      </Box>
    );
}

export default Contact;
