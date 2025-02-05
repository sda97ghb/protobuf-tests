# Protobuf tests

## Empty values

Results with empty message (empty bytes sequence `b""`).

`value` means `Message.FromString(b"").<field_name>`.

`HasField` means `Message.FromString(b"").HasField("<field_name>")`

<table>
    <thead>
        <tr>
            <th rowspan="2">Cardinality</th>
            <th colspan="2">string</th>
            <th colspan="2">int32</th>
            <th colspan="2">embedded message</th>
        </tr>
        <tr>
            <th>value</th>
            <th>HasField</th>
            <th>value</th>
            <th>HasField</th>
            <th>value</th>
            <th>HasField</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><i>(implicit)</i></td>
            <td>""<br><i>(empty string)</i></td>
            <td>💥</td>
            <td>0</td>
            <td>💥</td>
            <td>embedded message with all fields set to default</td>
            <td>False</td>
        </tr>
        <tr>
            <td>optional</td>
            <td>""<br><i>(empty string)</i></td>
            <td>False</td>
            <td>0</td>
            <td>False</td>
            <td>embedded message with all fields set to default</td>
            <td>False</td>
        </tr>
        <tr>
            <td>repeated</td>
            <td>[ ]<br><i>(empty list)</i></td>
            <td>💥</td>
            <td>[ ]<br><i>(empty list)</i></td>
            <td>💥</td>
            <td>[ ]<br><i>(empty list)</i></td>
            <td>💥</td>
        </tr>
    </tbody>
</table>

* 💥 - means `ValueError: Field Person.<field_name> does not have presence.`
