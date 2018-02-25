const astrocadePalette = [
    "#000000", "#242424", "#484848", "#6D6D6D", "#919191", "#B6B6B6", "#DADADA", "#FFFFFF",
    "#2500BB", "#4900E0", "#6E11FF", "#9235FF", "#B75AFF", "#DB7EFF", "#FFA3FF", "#FFC7FF",
    "#4900B0", "#6D00D5", "#9201F9", "#B625FF", "#DA4AFF", "#FF6EFF", "#FF92FF", "#FFB7FF",
    "#6A009F", "#8E00C3", "#B300E7", "#D718FF", "#FB3CFF", "#FF61FF", "#FF85FF", "#FFA9FF",
    "#870087", "#AB00AB", "#D000D0", "#F40EF4", "#FF32FF", "#FF56FF", "#FF7BFF", "#FF9FFF",
    "#9F006A", "#C3008E", "#E700B3", "#FF07D7", "#FF2CFB", "#FF50FF", "#FF74FF", "#FF99FF",
    "#B00049", "#D5006D", "#F90092", "#FF05B6", "#FF29DA", "#FF4DFF", "#FF72FF", "#FF96FF",
    "#BB0025", "#E00049", "#FF006E", "#FF0692", "#FF2AB7", "#FF4FDB", "#FF73FF", "#FF98FF",
    "#BF0000", "#E30024", "#FF0048", "#FF0B6D", "#FF3091", "#FF54B6", "#FF79DA", "#FF9DFF",
    "#BB0000", "#E00000", "#FF0023", "#FF1447", "#FF396C", "#FF5D90", "#FF82B5", "#FFA6D9",
    "#B00000", "#D50000", "#F90000", "#FF2124", "#FF4548", "#FF6A6C", "#FF8E91", "#FFB3B5",
    "#9F0000", "#C30000", "#E70C00", "#FF3003", "#FF5527", "#FF794B", "#FF9E70", "#FFC294",
    "#870000", "#AB0000", "#D01E00", "#F44200", "#FF670A", "#FF8B2E", "#FFAF53", "#FFD477",
    "#6A0000", "#8E0D00", "#B33100", "#D75600", "#FB7A00", "#FF9E17", "#FFC33B", "#FFE75F",
    "#490000", "#6D2100", "#924500", "#B66A00", "#DA8E00", "#FFB305", "#FFD729", "#FFFC4E",
    "#251100", "#493500", "#6E5A00", "#927E00", "#B7A300", "#DBC700", "#FFEB1E", "#FFFF43",
    "#002500", "#244900", "#486D00", "#6D9200", "#91B600", "#B6DB00", "#DAFF1B", "#FFFF3F",
    "#003700", "#005B00", "#238000", "#47A400", "#6CC900", "#90ED00", "#B5FF1E", "#D9FF43",
    "#004700", "#006C00", "#009000", "#24B400", "#48D900", "#6CFD05", "#91FF29", "#B5FF4E",
    "#005500", "#007900", "#009D00", "#03C200", "#27E600", "#4BFF17", "#70FF3B", "#94FF5F",
    "#005F00", "#008300", "#00A800", "#00CC00", "#0AF00A", "#2EFF2E", "#53FF53", "#77FF77",
    "#006500", "#008A00", "#00AE00", "#00D203", "#00F727", "#17FF4B", "#3BFF70", "#5FFF94",
    "#006800", "#008C00", "#00B100", "#00D524", "#00F948", "#05FF6C", "#29FF91", "#4EFFB5",
    "#006600", "#008B00", "#00AF23", "#00D447", "#00F86C", "#00FF90", "#1EFFB5", "#43FFD9",
    "#006100", "#008524", "#00AA48", "#00CE6D", "#00F391", "#00FFB6", "#1BFFDA", "#3FFFFE",
    "#005825", "#007C49", "#00A16E", "#00C592", "#00EAB7", "#00FFDB", "#1EFFFF", "#43FFFF",
    "#004B49", "#00706D", "#009492", "#00B9B6", "#00DDDA", "#05FFFF", "#29FFFF", "#4EFFFF",
    "#003C6A", "#00608E", "#0085B3", "#00A9D7", "#00CEFB", "#17F2FF", "#3BFFFF", "#5FFFFF",
    "#002A87", "#004FAB", "#0073D0", "#0097F4", "#0ABCFF", "#2EE0FF", "#53FFFF", "#77FFFF",
    "#00179F", "#003BC3", "#0060E7", "#0384FF", "#27A8FF", "#4BCDFF", "#70F1FF", "#94FFFF",
    "#0002B0", "#0027D5", "#004BF9", "#2470FF", "#4894FF", "#6CB9FF", "#91DDFF", "#B5FFFF",
    "#0000BB", "#0013E0", "#2337FF", "#475BFF", "#6C80FF", "#90A4FF", "#B5C9FF", "#D9EDFF"
]
const astrocadeSpectrum = [
    ["#000000", "#242424", "#484848", "#6D6D6D", "#919191", "#B6B6B6", "#DADADA", "#FFFFFF"],
    ["#2500BB", "#4900E0", "#6E11FF", "#9235FF", "#B75AFF", "#DB7EFF", "#FFA3FF", "#FFC7FF"],
    ["#4900B0", "#6D00D5", "#9201F9", "#B625FF", "#DA4AFF", "#FF6EFF", "#FF92FF", "#FFB7FF"],
    ["#6A009F", "#8E00C3", "#B300E7", "#D718FF", "#FB3CFF", "#FF61FF", "#FF85FF", "#FFA9FF"],
    ["#870087", "#AB00AB", "#D000D0", "#F40EF4", "#FF32FF", "#FF56FF", "#FF7BFF", "#FF9FFF"],
    ["#9F006A", "#C3008E", "#E700B3", "#FF07D7", "#FF2CFB", "#FF50FF", "#FF74FF", "#FF99FF"],
    ["#B00049", "#D5006D", "#F90092", "#FF05B6", "#FF29DA", "#FF4DFF", "#FF72FF", "#FF96FF"],
    ["#BB0025", "#E00049", "#FF006E", "#FF0692", "#FF2AB7", "#FF4FDB", "#FF73FF", "#FF98FF"],
    ["#BF0000", "#E30024", "#FF0048", "#FF0B6D", "#FF3091", "#FF54B6", "#FF79DA", "#FF9DFF"],
    ["#BB0000", "#E00000", "#FF0023", "#FF1447", "#FF396C", "#FF5D90", "#FF82B5", "#FFA6D9"],
    ["#B00000", "#D50000", "#F90000", "#FF2124", "#FF4548", "#FF6A6C", "#FF8E91", "#FFB3B5"],
    ["#9F0000", "#C30000", "#E70C00", "#FF3003", "#FF5527", "#FF794B", "#FF9E70", "#FFC294"],
    ["#870000", "#AB0000", "#D01E00", "#F44200", "#FF670A", "#FF8B2E", "#FFAF53", "#FFD477"],
    ["#6A0000", "#8E0D00", "#B33100", "#D75600", "#FB7A00", "#FF9E17", "#FFC33B", "#FFE75F"],
    ["#490000", "#6D2100", "#924500", "#B66A00", "#DA8E00", "#FFB305", "#FFD729", "#FFFC4E"],
    ["#251100", "#493500", "#6E5A00", "#927E00", "#B7A300", "#DBC700", "#FFEB1E", "#FFFF43"],
    ["#002500", "#244900", "#486D00", "#6D9200", "#91B600", "#B6DB00", "#DAFF1B", "#FFFF3F"],
    ["#003700", "#005B00", "#238000", "#47A400", "#6CC900", "#90ED00", "#B5FF1E", "#D9FF43"],
    ["#004700", "#006C00", "#009000", "#24B400", "#48D900", "#6CFD05", "#91FF29", "#B5FF4E"],
    ["#005500", "#007900", "#009D00", "#03C200", "#27E600", "#4BFF17", "#70FF3B", "#94FF5F"],
    ["#005F00", "#008300", "#00A800", "#00CC00", "#0AF00A", "#2EFF2E", "#53FF53", "#77FF77"],
    ["#006500", "#008A00", "#00AE00", "#00D203", "#00F727", "#17FF4B", "#3BFF70", "#5FFF94"],
    ["#006800", "#008C00", "#00B100", "#00D524", "#00F948", "#05FF6C", "#29FF91", "#4EFFB5"],
    ["#006600", "#008B00", "#00AF23", "#00D447", "#00F86C", "#00FF90", "#1EFFB5", "#43FFD9"],
    ["#006100", "#008524", "#00AA48", "#00CE6D", "#00F391", "#00FFB6", "#1BFFDA", "#3FFFFE"],
    ["#005825", "#007C49", "#00A16E", "#00C592", "#00EAB7", "#00FFDB", "#1EFFFF", "#43FFFF"],
    ["#004B49", "#00706D", "#009492", "#00B9B6", "#00DDDA", "#05FFFF", "#29FFFF", "#4EFFFF"],
    ["#003C6A", "#00608E", "#0085B3", "#00A9D7", "#00CEFB", "#17F2FF", "#3BFFFF", "#5FFFFF"],
    ["#002A87", "#004FAB", "#0073D0", "#0097F4", "#0ABCFF", "#2EE0FF", "#53FFFF", "#77FFFF"],
    ["#00179F", "#003BC3", "#0060E7", "#0384FF", "#27A8FF", "#4BCDFF", "#70F1FF", "#94FFFF"],
    ["#0002B0", "#0027D5", "#004BF9", "#2470FF", "#4894FF", "#6CB9FF", "#91DDFF", "#B5FFFF"],
    ["#0000BB", "#0013E0", "#2337FF", "#475BFF", "#6C80FF", "#90A4FF", "#B5C9FF", "#D9EDFF"]
]
let tool = 'draw';
let currentDrawPal = "01";
let currentLeft00 = astrocadePalette[0x00];
let currentLeft01 = astrocadePalette[0x44];
let currentLeft02 = astrocadePalette[0xEF];
let currentLeft03 = astrocadePalette[0x77];
let currentRight00 = astrocadePalette[0x00];
let currentRight01 = astrocadePalette[0xCC];
let currentRight02 = astrocadePalette[0x4F];
let currentRight03 = astrocadePalette[0x08];
let colorBoundaryPos = 84;
let isBoundaryVisible = true;
let screenwidth = 160;
let screenheight = 102;
let pixel = $(".pixel");
let imgarray = [];
let exportdata = ""



$(".left00").css("background-color", currentLeft00);
$(".left01").css("background-color", currentLeft01);
$(".left02").css("background-color", currentLeft02);
$(".left03").css("background-color", currentLeft03);
$(".right00").css("background-color", currentRight00);
$(".right01").css("background-color", currentRight01);
$(".right02").css("background-color", currentRight02);
$(".right03").css("background-color", currentRight03);

// // Draw empty screen
drawAstrocadeScreen(screenwidth, screenheight);

setuppal1();

$("input[name='palselect']").on("click", function () {
    currentDrawPal = $("input:checked").val();
});

$("input[id='boundarytoggle']").on("click", function () {
    isBoundaryVisible = $("input[id='boundarytoggle']")[0].checked;
    redrawColorBoundary(screenwidth, screenheight, colorBoundaryPos, "none");
});

$("input[id='gridtoggle']").on("click", function () {
    isGridVisible = $("input[id='gridtoggle']")[0].checked;
    if (isGridVisible) {
        $(".pixel", "#screen").css({"border":".25px solid #0e0e0e"});
        isBoundaryVisible = $("input[id='boundarytoggle']")[0].checked;
        redrawColorBoundary(screenwidth, screenheight, colorBoundaryPos, "none");
        $("input[id='boundarytoggle']").attr({'disabled': false});
    }
    else { 
        $(".pixel", "#screen").css({"border":"0"});
        isBoundaryVisible = false;
        $("input[id='boundarytoggle']").attr({'disabled': true});
 }
});

// Click handler for turning on individual pixel
document.getElementById("screen").addEventListener("mousedown", function (e) {
    if (e.target && e.target.matches("div.pixel")) { colorPixel(e) }
});

// Mouseover handler for click-and-drag drawing
document.getElementById("screen").addEventListener("mouseover", function (e) {
    if (e.target && e.target.matches("div.pixel") && (e.buttons == 1)) { colorPixel(e) }
});

$("html").keyup(function (event) {
    if (event.which == 37) {
        event.preventDefault();
        redrawColorBoundary(screenwidth, screenheight, colorBoundaryPos, "left");
        fixColorBoundaryBufferZone2(screenwidth, screenheight, colorBoundaryPos, "left")
    }
    else if (event.which == 39) {
        event.preventDefault();
        redrawColorBoundary(screenwidth, screenheight, colorBoundaryPos, "right");
        fixColorBoundaryBufferZone2(screenwidth, screenheight, colorBoundaryPos, "right")
    }
});

function drawAstrocadeScreen(screenwidth, screenheight) {
    for (i = 0; i < screenwidth * screenheight; i++) {
        let createpixel = document.createElement("div");
        let row = Math.ceil(i / screenwidth);
        // If pixel is to the left of the color boundary...
        if (Math.ceil(i % 160 == 0) || (colorBoundaryPos > 160 - (screenwidth * row - i))) {
            document.getElementById("screen").appendChild(createpixel).className = "pixel left00";
        }
        // If pixel is to the right of the color boundary...
        else {
            document.getElementById("screen").appendChild(createpixel).className = "pixel right00";
        }
    }
    $(".left00").css("background-color", currentLeft00);
    $(".right00").css("background-color", currentRight00);
    redrawColorBoundary(screenwidth, screenheight, colorBoundaryPos, "none");
}

function colorPixel(clicked) {
    let row = Math.ceil($(clicked.target).index() / screenwidth);
    // If drawing is to the right of the boundary...
    if ((Math.ceil($(clicked.target).index() % 160 == 0) || (colorBoundaryPos > 160 - (screenwidth * row - $(clicked.target).index())))) {
        if (currentDrawPal == "00") {
            $(clicked.target).css("background-color", currentLeft00);
            clicked.target.className = "pixel " + "left00";
        }
        else if (currentDrawPal == "01") {
            $(clicked.target).css("background-color", currentLeft01);
            clicked.target.className = "pixel " + "left01";
        }
        else if (currentDrawPal == "02") {
            $(clicked.target).css("background-color", currentLeft02);
            clicked.target.className = "pixel " + "left02";
        }
        else if (currentDrawPal == "03") {
            $(clicked.target).css("background-color", currentLeft03);
            clicked.target.className = "pixel " + "left03";
        }
    }
    else {
        if (currentDrawPal == "00") {
            $(clicked.target).css("background-color", currentRight00);
            clicked.target.className = "pixel " + "right00";
        }
        else if (currentDrawPal == "01") {
            $(clicked.target).css("background-color", currentRight01);
            clicked.target.className = "pixel " + "right01";
        }
        else if (currentDrawPal == "02") {
            $(clicked.target).css("background-color", currentRight02);
            clicked.target.className = "pixel " + "right02";
        }
        else if (currentDrawPal == "03") {
            $(clicked.target).css("background-color", currentRight03);
            clicked.target.className = "pixel " + "right03";
        }
    }
}

function redrawColorBoundary(screenwidth, screenheight, loc, direction) {
    if (direction == "left") {
        for (i = loc; i < screenheight * screenwidth; i = i + screenwidth) {
            $(".pixel", "#screen").eq(i).css("border", ".25px solid #0e0e0e");
            if (isBoundaryVisible) {
                $(".pixel", "#screen").eq(i - 4).css("border-left", ".25px solid rgba(243, 89, 62, 1)");
            }
            else {
                $(".pixel", "#screen").eq(i - 4).css("border-left", ".25px solid #0e0e0e");
            }

        }
        colorBoundaryPos = colorBoundaryPos - 4;
    }
    else if (direction == "right") {
        for (i = loc; i < screenheight * screenwidth; i = i + screenwidth) {
            $(".pixel", "#screen").eq(i).css("border", ".25px solid #0e0e0e");
            if (isBoundaryVisible) {
                $(".pixel", "#screen").eq(i + 4).css("border-left", ".25px solid rgba(243, 89, 62, 1)");
            }
            else {
                $(".pixel", "#screen").eq(i + 4).css("border-left", ".25px solid #0e0e0e");
           }
        }
        colorBoundaryPos = colorBoundaryPos + 4;
    }
    else {
        for (i = loc; i < screenheight * screenwidth; i = i + screenwidth) {
            $(".pixel", "#screen").eq(i).css("border", ".25px solid #0e0e0e");
            if (isBoundaryVisible) {
                $(".pixel", "#screen").eq(i).css("border-left", ".25px solid rgba(243, 89, 62, 1)");
            }
            else {
              //  $(".pixel", "#screen").eq(i).css("border-left", ".25px solid #0e0e0e");
            }
        }
    }
}

function fixColorBoundaryBufferZone2(screenwidth, screenheight, loc, dir){
    if (dir == "left") {
        let a = 0;
        let b = 4;
        for (j = a; j < b; j++) {
            for (i = loc + j; i < screenheight * screenwidth; i = i + screenwidth) {
                if ($(".pixel", "#screen").eq(i)[0].className == "pixel left00") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel right00"
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left01") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel right01";
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left02") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel right02"
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left03") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel right03"
                }
            }
        }
    }
    else if (dir == "right") {
        let a = -4;
        let b = 0;
        for (j = a; j < b; j++) {
            for (i = loc + j; i < screenheight * screenwidth; i = i + screenwidth) {
                if ($(".pixel", "#screen").eq(i)[0].className == "pixel right00") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel left00"
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right01") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel left01"
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right02") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel left02"
                }
                else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right03") {
                    $(".pixel", "#screen").eq(i)[0].className = "pixel left03"
                }
            }
        }
    }
    $( ".left00" ).css( "background-color", currentLeft00 );
    $( ".left01" ).css( "background-color", currentLeft01 );
    $( ".left02" ).css( "background-color", currentLeft02 );
    $( ".left03" ).css( "background-color", currentLeft03 );
    $( ".right00" ).css( "background-color", currentRight00 );
    $( ".right01" ).css( "background-color", currentRight01 );
    $( ".right02" ).css( "background-color", currentRight02 );
    $( ".right03" ).css( "background-color", currentRight03 );
}
function fixColorBoundaryBufferZone(screenwidth, screenheight, loc, dir) {
    let a = -4;
    let b = 0;
    if (dir == "left") {
        a = 0;
        b = 4;
    }
    for (j = a; j < b; j++) {
        for (i = loc + j; i < screenheight * screenwidth; i = i + screenwidth) {
            if ($(".pixel", "#screen").eq(i)[0].className == "pixel left00") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel right00"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right00") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel left00"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left01") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel right01";
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right01") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel left01"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left02") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel right02"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right02") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel left02"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel left03") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel right03"
            }
            else if ($(".pixel", "#screen").eq(i)[0].className == "pixel right03") {
                $(".pixel", "#screen").eq(i)[0].className = "pixel left03"
            }
        }
    }
    $( ".left00" ).css( "background-color", currentLeft00 );
    $( ".left01" ).css( "background-color", currentLeft01 );
    $( ".left02" ).css( "background-color", currentLeft02 );
    $( ".left03" ).css( "background-color", currentLeft03 );
    $( ".right00" ).css( "background-color", currentRight00 );
    $( ".right01" ).css( "background-color", currentRight01 );
    $( ".right02" ).css( "background-color", currentRight02 );
    $( ".right03" ).css( "background-color", currentRight03 );
}

document.getElementById("download").addEventListener("click", function (e) {
    let pixels = document.querySelectorAll("div.pixel")
    exportdata = ""
    for (i = 0; i < (pixels.length / 4); i++) {
        imgarray[i] = 0;
        if ((pixels[i * 4].className == "pixel left01") || (pixels[i * 4].className == "pixel right01")) {
            imgarray[i] += 0x40;
        }
        else if (pixels[i * 4].className == "pixel left02" || pixels[i * 4].className == "pixel right02") {
            imgarray[i] += 0x80;
        }
        else if (pixels[i * 4].className == "pixel left03" || pixels[i * 4].className == "pixel right03") {
            imgarray[i] += 0xC0;
        }
        if (pixels[i * 4 + 1].className == "pixel left01" || pixels[i * 4 + 1].className == "pixel right01") {
            imgarray[i] += 0x10;
        }
        else if (pixels[i * 4 + 1].className == "pixel left02" || pixels[i * 4 + 1].className == "pixel right02") {
            imgarray[i] += 0x20;
        }
        else if (pixels[i * 4 + 1].className == "pixel left03" || pixels[i * 4 + 1].className == "pixel right03") {
            imgarray[i] += 0x30;
        }
        if (pixels[i * 4 + 2].className == "pixel left01" || pixels[i * 4 + 2].className == "pixel right01") {
            imgarray[i] += 0x04;
        }
        else if (pixels[i * 4 + 2].className == "pixel left02" || pixels[i * 4 + 2].className == "pixel right02") {
            imgarray[i] += 0x08;
        }
        else if (pixels[i * 4 + 2].className == "pixel left03" || pixels[i * 4 + 2].className == "pixel right03") {
            imgarray[i] += 0x0C;
        }
        if (pixels[i * 4 + 3].className == "pixel left01" || pixels[i * 4 + 3].className == "pixel right01") {
            imgarray[i] += 0x01;
        }
        else if (pixels[i * 4 + 3].className == "pixel left02" || pixels[i * 4 + 3].className == "pixel right02") {
            imgarray[i] += 0x02;
        }
        else if (pixels[i * 4 + 3].className == "pixel left03" || pixels[i * 4 + 3].className == "pixel right03") {
            imgarray[i] += 0x03;
        }
    }

    // Export .asm
    let asmsrc = ""
    for (i=0; i<imgarray.length;) {
        asmsrc = asmsrc + "\nDB $" + imgarray[i].toString(16) + ", $" + imgarray[i+1].toString(16) + ", $" + imgarray[i+2].toString(16) + ", $" + imgarray[i+3].toString(16) + ", $" + imgarray[i+4].toString(16);
        i = i+5;
    }

    // Export binary
    // let blob = new Blob([Uint8Array.from(imgarray)], { type: "application/octet-stream" })

    let blob = new Blob([asmsrc], { type: "text" })
    saveAs(blob, "astropaint.gfx")


});

function setuppal1(){
    $("#left00").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x00],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        change: function(color) {
            currentLeft00 = color.toHexString()
            $( ".left00" ).css( "background-color", currentLeft00 );
        },
        palette: astrocadeSpectrum
    });
    $("#left01").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x44],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentLeft01 = color.toHexString()
            $( ".left01" ).css( "background-color", currentLeft01 );
        },
        palette: astrocadeSpectrum
    });
    $("#left02").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0xEE],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentLeft02 = color.toHexString()
            $( ".left02" ).css( "background-color", currentLeft02 );
        },
        palette: astrocadeSpectrum
    });
    $("#left03").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x77],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentLeft03 = color.toHexString()
            $( ".left03" ).css( "background-color", currentLeft03 );
        },
        palette: astrocadeSpectrum
    });
    $("#right00").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x00],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentRight00 = color.toHexString()
            $( ".right00" ).css( "background-color", currentRight00 );
        },
        palette: astrocadeSpectrum
    });
    $("#right01").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0xCC],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentRight01 = color.toHexString()
            $( ".right01" ).css( "background-color", currentRight01 );
        },
        palette: astrocadeSpectrum
    });
    $("#right02").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x4F],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentRight02 = color.toHexString()
            $( ".right02" ).css( "background-color", currentRight02 );
        },
        palette: astrocadeSpectrum
    });
    $("#right03").spectrum({
        showPaletteOnly: true,
        showPalette: true,
        color: astrocadePalette[0x0B],
        showPaletteOnly: true,
        hideAfterPaletteSelect: true,
        hide: function(color) {
            currentRight03 = color.toHexString()
            $( ".right03" ).css( "background-color", currentRight03 );
        },
        palette: astrocadeSpectrum
    });
}
