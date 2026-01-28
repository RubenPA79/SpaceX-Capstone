$pptxPath = "c:\Users\CELTI\Desktop\laboratorio\Final_Presentation_Spacex.pptx"
$pdfPath = "c:\Users\CELTI\Desktop\laboratorio\Final_Presentation_Spacex.pdf"

try {
    $ppt = New-Object -ComObject PowerPoint.Application
    # $ppt.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $presentation = $ppt.Presentations.Open($pptxPath)
    $presentation.SaveAs($pdfPath, 32) # 32 is ppSaveAsPDF
    $presentation.Close()
    $ppt.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
    Write-Host "Success: PDF created at $pdfPath"
} catch {
    Write-Error "Failed to convert. Ensure Microsoft PowerPoint is installed."
    Write-Error $_.Exception.Message
}
