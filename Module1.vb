Module Module1

    Sub Main()
        Dim list() As Integer = {67, 25, 92, 49, 38, 72, 99, 54}

        Dim temporary As Integer

        For i = 0 To list.Length - 1
            Console.Write(list(i) & " ")

        Next
        Console.WriteLine()
        'While changes = True
        For j = 0 To list.Length - 1
            For i = 0 To list.Length - 2
                If list(i) < list(i + 1) Then

                    list(i) = list(i)

                Else
                    temporary = list(i)
                    list(i) = list(i + 1)

                End If

            Next
        Next 'End While
        For i = 0 To list.Length - 1
                Console.Write(list(i) & " ")

            Next
        Console.WriteLine()

        Console.ReadLine()
    End Sub
End Module